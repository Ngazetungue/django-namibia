from django.shortcuts import render

def home(request):
    return render(request, "website/home.html")

def about(request):
    return render(request, "website/about.html")

def coc(request):
    return render(request, "website/coc.html")

def resources(request):
    return render(request, "website/resources.html")

def signup(request):
    return render(request, "website/signup.html")

def login(request):
    return render(request, "website/login.html")