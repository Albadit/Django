from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.Register, name="register"),

    path("profile/<int:pk>/", views.edit_profile, name="profile"),

    path("addbook/", views.AddBook, name="addbook"),
    path("books/", views.AllBooks, name="books"),

    path("unapproved_books/", views.unapproved_books, name="unapproved_books"),
    path("approve_book/<int:pk>", views.approve_book, name="approve_book"),
    path("deny_book/<int:pk>", views.deny_book, name="deny_book"),

    path("remove_book/<int:pk>", views.remove_book, name="remove_book"),
    path("editbook/<int:pk>/", views.EditBook, name="editbook"),

    path('addreadaction/', views.addreadaction, name='addreadaction'),
    
    path('readings/', views.readings, name='readings'),
    path("remove_read/<int:pk>", views.remove_read, name="remove_read"),

    path('login/', views.login, name='login'),
]