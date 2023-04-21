from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from .forms import ProfileForm, BookForm, ReadForm, SingupForm
from .models import Profile, Book, Read

from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# home page
def home(request):
    return render(request, 'base/home.html')

# login / signup
def re_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            context = {"error": 'Invalid login credentials'}
            return render(request, 'registration/login.html', context)
    else:
        return render(request, 'registration/login.html')

def singup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SingupForm()
    return render(request, 'registration/signup.html', {'form': form})

# profile
@login_required
def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(id = user.id)
    context = {'user': user, 'profile': profile}
    return render(request, 'base/profile.html', context)

@login_required
def edit_profile(request, pk):
    profile = Profile.objects.get(user_id=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)       
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully!')
        else:
            messages.error(request, 'Profile updated didn\'t succeed!')
    else:
        form = ProfileForm()
    context = {'form': form, 'profile': profile}
    return render(request, 'base/profile.html', context)

# books
def books(request):
    books = Book.objects.filter(Approved=True)
    context = {'books': books}
    return render(request, 'base/books.html', context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added succesfully')
            return redirect('home')
        else:
            messages.error(request, 'Book wasn\'t added succesfully')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'base/add_book.html', context)

@staff_member_required
def edit_book(request, pk):
    book = Book.objects.get(id = pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book edited succesfully')
            return redirect('books')
        else:
            messages.error(request, 'Book edit failed') 
    else:
        form = BookForm()
    context = {'form': form, 'book': book}
    return render(request, 'base/edit_book.html', context)

@staff_member_required
def remove_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, "Book removed.")
    return redirect('books')

@staff_member_required
def unapproved_books(request):
    books = Book.objects.filter(Approved=False)
    context = {'books': books}
    return render(request, 'base/unapproved_books.html', context)

@staff_member_required
def approve_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.Approved = True
    book.Approved_by = request.user
    book.save()
    messages.success(request, 'Book approved.')
    return redirect('unapproved_books')

@staff_member_required
def deny_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, 'Book denied.')
    return redirect('unapproved_books')

# read action
def readings(request):
    book_dict = {book.pk: {'name': book.Title} for book in Book.objects.all()}
    user_dict = {user.pk: user.username for user in User.objects.all()}
    readings = Read.objects.all()

    readers = {
        i.id: {
            'name': book_dict.get(i.Book_id)['name'],
            'user': user_dict.get(i.User_id),
            'score': i.Score,
            'date': i.Date
        }
        for i in readings
    }
    readers_sorted = dict(sorted(readers.items(), key=lambda x: x[1]['date']))

    context = {'readers': readers_sorted}
    return render(request, 'base/readings.html', context)

@login_required
def add_read_action(request):
    books = Book.objects.filter(Approved=True)
    scores = list(range(1, 11))

    if request.method == 'POST':
        form = ReadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Read action added succesfully')
            return redirect('home')
        else:
            messages.error(request, 'Read action has not been added')
    else:
        form = ReadForm()
    
    context = {'form': form, 'books': books, 'scores': scores}
    return render(request, 'base/add_read_action.html', context)


@staff_member_required
def remove_read(request, pk):
    read = Read.objects.get(id=pk)
    read.delete()
    messages.success(request, 'Read action removed.')
    return redirect('readings')
