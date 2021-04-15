from django.shortcuts import render

def home(request):
    return render(request, "web/home.html")

def sample(request):
    return render(request, "web/sample.html")

def error_page(request):
    return render(request, "web/error_page.html")