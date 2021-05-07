from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only

from django.contrib.auth.models import User

from .forms import IMCForm, PesoCorregidoForm, GERForm

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
    context = {}
    form = IMCForm()
    if request.method == 'POST':
        form = IMCForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'core/formulas/imc.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def pesoCorregido(request):
    context = {}
    form = PesoCorregidoForm()
    if request.method == 'POST':
        form = PesoCorregidoForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'core/formulas/pesocorregido.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def ger(request):
    context = {}
    form = GERForm()
    if request.method == 'POST':
        form = GERForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'core/formulas/ger.html', context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def gruposNutricionales(request):
    return render(request, 'core/formulas/gruposnutricionales.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def dieta(request):
    return render(request, 'core/formulas/dietas.html')
