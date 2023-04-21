from django.shortcuts import redirect, render

from .forms import BookForm, ProfileForm, ReadForm

from .models import Book, Profile, Read

from django.db import connection
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
            return redirect("books")
        else:
            messages.error(request, "Book wasn't added succesfully")
    else:
        form = BookForm()
    
    context = {"form": form}
    return render(request, "base/addbook.html", context)

@staff_member_required
def EditBook(request, pk):
    book = Book.objects.get(id = pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book edited succesfully")
            return redirect("books")
        else:
            messages.error(request, "Book edit failed") 
    else:
        form = BookForm()
    
    context = {"form": form, "book": book}
    return render(request, "base/editbook.html", context)

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
def profile(request, pk):
    profile = Profile.objects.get(user_id=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)       

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated succesfully!")
        else:
            messages.error(request, "Profile updated didn't succeed!")
    else:
        form = ProfileForm()

    context = {"form": form, "profile": profile}

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

@staff_member_required
def remove_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, "Book removed.")
    return redirect("books")

@login_required
def addreadaction(request):
    books = Book.objects.filter(Approved=True)

    if request.method == "POST":
        form = ReadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Read action added succesfully")
            return redirect("index")
        else:
            messages.error(request, "Read action has not been added")
    else:
        form = ReadForm()
    
    context = {"form": form, "books": books}
    return render(request, "base/addreadaction.html", context)

def readings(request):
    query = """SELECT base_book.Title, auth_user.username, base_read.Score, base_read.Date, base_read.id FROM base_read
    JOIN base_book ON base_read.Book_id == base_book.id
    JOIN auth_user ON base_read.User_id == auth_user.id"""

    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        readings = [dict(zip(columns, row))
                    for row in cursor.fetchall()]
    context = {"readings": readings}
    return render(request, 'base/readings.html', context)

@login_required
def user_readings(request, pk):
    query = """SELECT base_book.Title, auth_user.username, base_read.Score, base_read.Date, base_read.id FROM base_read
    JOIN base_book ON base_read.Book_id == base_book.id
    JOIN auth_user ON base_read.User_id == auth_user.id
    WHERE base_read.User_id= %s"""

    with connection.cursor() as cursor:
        cursor.execute(query, [pk])
        columns = [col[0] for col in cursor.description]
        readings = [dict(zip(columns, row)) for row in cursor.fetchall()]
    context = {"readings": readings}
    return render(request, 'base/userreadings.html', context)

@login_required
def editreadings(request, pk):
    books = Book.objects.filter(Approved=True)
    read = Read.objects.get(id=pk)
    
    if request.method == "POST":
        form = ReadForm(request.POST, instance=read)
        if form.is_valid():
            form.save()
            messages.success(request, "Read action edited succesfully")
            return redirect("userreadings", read.User_id)
        else:
            messages.error(request, "Read action has not been edited")
    else:
        form = ReadForm()
    
    context = {"form": form, "books": books, "read": read}
    return render(request, "base/editreading.html", context)

@staff_member_required
def remove_read(request, pk):
    read = Read.objects.get(id=pk)
    read.delete()
    messages.success(request, "Read action removed.")
    return redirect("readings")
