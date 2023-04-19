from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("profile/<str:username>/", views.get_user_profile, name="profile"),
    path("addbook/", views.AddBook, name="addbook"),
    path("books/", views.AllBooks, name="books"),

    path("unapproved_books/", views.unapproved_books, name="unapproved_books"),
    path("approve_book/<int:pk>", views.approve_book, name="approve_book"),
    path("deny_book/<int:pk>", views.deny_book, name="deny_book"),
]