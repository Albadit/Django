from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", include("django.contrib.auth.urls")),
    path("re_login/", views.re_login, name="re_login"),
    path("signup/", views.singup, name="signup"),

    path("profile/<int:pk>/", views.profile, name="profile"),
    path("edit_profile/<int:pk>/", views.edit_profile, name="edit_profile"),

    path("books/", views.books, name="books"),
    path("add_book/", views.add_book, name="add_book"),
    path("remove_book/<int:pk>", views.remove_book, name="remove_book"),
    path("edit_book/<int:pk>", views.edit_book, name="edit_book"),

    path("unapproved_books/", views.unapproved_books, name="unapproved_books"),
    path("approve_book/<int:pk>", views.approve_book, name="approve_book"),
    path("deny_book/<int:pk>", views.deny_book, name="deny_book"),

    path('readings/', views.readings, name='readings'),
    path('your_readings/<int:pk>', views.your_readings, name='your_readings'),
    path('add_read_action/', views.add_read_action, name='add_read_action'),
    path('edit_read_action/<int:pk>', views.edit_read_action, name='edit_read_action'),
    path("remove_read/<int:pk>", views.remove_read, name="remove_read"),
]