from django.shortcuts import redirect, render

from .forms import BookForm, ReadForm, CustomUserCreationForm
from .models import Book, Profile

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "base/index.html")

def AllBooks(request):
    books = Book.objects.filter(Approved=True)
    context = {"books": books}
    return render(request, "base/books.html", context)

def Login(request):
    context = {"error": 'Invalid login credentials'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', context)
    else:
        return render(request, 'registration/login.html', context)


def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def AddBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Book added succesfully")
            return redirect("index")
    else:
        form = BookForm()
    
    context = {"form": form}
    return render(request, "base/addbook.html", context)

@login_required
def get_user_profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(id = user.id)
    context = {"user": user, "profile": profile}
    return render(request, "base/profile.html", context)

@staff_member_required
def unapproved_books(request):
    books = Book.objects.filter(Approved=False)
    context = {"books": books}
    return render(request, "base/unapproved_books.html", context)

@staff_member_required
def approve_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.Approved = True
    book.Approved_by = request.user
    book.save()
    messages.success(request, "Book approved.")
    return redirect("unapproved_books")

@staff_member_required
def deny_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, "Book denied.")
    return redirect("unapproved_books")
