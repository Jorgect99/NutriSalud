from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponseRedirect, redirect

from registration.forms import LoginForm, SignupForm
from .decorators import unauthenticated_user, allow_users

# Create your views here.
@unauthenticated_user
def signupPage(request):
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registration/login/?register')
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request, 'registration/registration.html', context)

@unauthenticated_user
def loginPage(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            password =  form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request, user) 
                if user.is_staff:
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/web')

            else:
                error = "Login Error"
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, 'registration/login.html', context)

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/web')

