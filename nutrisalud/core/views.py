from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only

from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
@admin_only
def home(request):
    return render(request, 'core/index-dashboard.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def clientes(request):  
    clientes = User.objects.filter(groups__name='cliente')
    context = {'clientes':clientes}
    return render(request, 'core/clientes.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def eliminarCliente(request, cliente_id):
    cliente = User.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('clientes')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def imc(request):
    return render(request, 'core/formulas/imc.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def met(request):
    return render(request, 'core/formulas/met.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def gruposNutricionales(request):
    return render(request, 'core/formulas/gruposnutricionales.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def dieta(request):
    return render(request, 'core/formulas/dietas.html')
