from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, HttpResponseRedirect

from accounts.forms import LoginForm

# Create your views here.

def registerPage(request):
    context = {}
    return render(request, 'accounts/registration.html', context)

def loginPage(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            password =  form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request, user) 
                return HttpResponseRedirect('/web')
            else:
                error = "Login Error"
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/login')


            
    



