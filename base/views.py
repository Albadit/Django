from django.shortcuts import redirect, render

from .forms import BookForm, ReadForm

from .models import Book, Profile

from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "base/index.html")

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

def AllBooks(request):
    books = Book.objects.filter(Approved=True)
    context = {"books": books}
    return render(request, "base/books.html", context)

def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    
    context = {"form": form}
    return render(request, "registration/register.html", context)

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
