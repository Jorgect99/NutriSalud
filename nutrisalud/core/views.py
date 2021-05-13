from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only

from django.contrib.auth.models import User

from .models import IMC, PesoCorregido, GER, Food_Group
from .forms import IMCForm, PesoCorregidoForm, GERForm, Food_GroupForm

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
            return redirect('lista_imc')
    context = {'form':form}
    return render(request, 'core/formulas/imc.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def eliminarCalculoIMC(request, imc_id):
    imc = IMC.objects.get(id=imc_id)
    imc.delete()
    return redirect('lista_imc')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def pesoCorregido(request):
    context = {}
    form = PesoCorregidoForm()
    if request.method == 'POST':
        form = PesoCorregidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pesocorregido')
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
            return redirect('lista_ger')
    context = {'form':form}
    return render(request, 'core/formulas/ger.html', context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def gruposNutricionales(request):
    context = {}
    form = Food_GroupForm()
    if request.method == 'POST':
        form = Food_GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_grupo_nutricional')
    context = {'form':form}
    return render(request, 'core/formulas/gruposnutricionales.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def lista_gruposNutricionales(request):  
    lista_gruposNutricionales = Food_Group.objects.all()
    context = {'lista_gruposNutricionales':lista_gruposNutricionales}
    return render(request, 'core/lista_gruposNutricionales.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def dieta(request):
    return render(request, 'core/formulas/dietas.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def lista_imc(request):  
    lista_imc = IMC.objects.all()
    context = {'lista_imc':lista_imc}
    return render(request, 'core/lista_imc.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def lista_pesocorregido(request):  
    lista_pesocorregido = PesoCorregido.objects.all()
    context = {'lista_pesocorregido':lista_pesocorregido}
    return render(request, 'core/lista_pesocorregido.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def lista_ger(request):  
    lista_ger = GER.objects.all()
    context = {'lista_ger':lista_ger}
    return render(request, 'core/lista_ger.html', context)