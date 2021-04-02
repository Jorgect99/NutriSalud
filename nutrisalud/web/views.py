from django.shortcuts import render

def home(request):
    return render(request, "web/home.html")

def sample(request):
    return render(request, "web/sample.html")