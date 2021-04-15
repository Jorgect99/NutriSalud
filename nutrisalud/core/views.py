from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only

# Create your views here.

@login_required(login_url='login')
@admin_only
def home(request):
    return render(request, 'core/index-dashboard.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def clientes(request):
    return render(request, 'core/clientes.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def imc(request):
    return render(request, 'core/formulas/imc.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def met(request):
    return render(request, 'core/formulas/met.html')

