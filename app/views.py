from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request ,'home.html')

def register(request):
    return render(request ,'register.html')

def login(request):
    return render(request ,'login.html')

def gallery(request):
    return render(request ,'gallery.html')

def about(request):
    return render(request ,'about.html')


def contact(request):
    return render(request ,'contact.html')