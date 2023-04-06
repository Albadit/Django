from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.Register, name="register"),
    path("profile/<str:username>/", views.get_user_profile, name="profile"),
]