from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"first_name" : "asd", "last_name" : "dsa", "age": 21}
    return render(request, 'base/index.html', context)