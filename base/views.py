from django.shortcuts import redirect, render

from .models import Profile

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "base/index.html")

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
    context = {"user": user}
    return render(request, "base/profile.html", context)
