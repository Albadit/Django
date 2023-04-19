from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	return render(request, 'base/home.html', context)

def login(request):
    context = {}
    return render(request, 'base/login.html', context)


def actie(request):
    context = {}
    return render(request, 'base/actie.html', context)
