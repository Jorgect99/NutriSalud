from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User

from .models import IMC, PesoCorregido, GER, Food_Group, Dieta
from .forms import IMCForm, PesoCorregidoForm, GERForm, Food_GroupForm, DietForm
from citas.models import *
from registration.models import *
from django.contrib import messages


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
    messages.success(request, "Eliminado Correctamente")
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
    messages.success(request, "Eliminado Correctamente")
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
@admin_only
def menu(request):
    return render(request, 'core/menu.html')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])    
def dieta(request):
    context = {}
    form = DietForm()
    if request.method == 'POST':
        form = DietForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_dieta')

    context = {'form':form, "action":"Agregar"}
    return render(request, 'core/formulas/dietas.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin']) 
def get_client_info(request, client_id):
    client = get_object_or_404(Profile, id=client_id)
    data = {
        "imc": client.get_imc(),
        "peso": client.get_peso(),
        "ger": client.get_ger(),
        "get": client.get_get(),
    }
    return JsonResponse(data, status=200)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def lista_dieta(request):  
    lista_dieta = Dieta.objects.all()
    context = {'lista_dieta':lista_dieta}
    return render(request, 'core/lista_dieta.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def editarCalculoDieta(request, dieta_id):
    context = {}
    dieta = Dieta.objects.get(id=dieta_id)
    form = DietForm(instance=dieta)
    if request.method == 'POST':
        form = DietForm(request.POST, instance=dieta)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado Correctamente")
            return redirect('lista_dieta')
    context = {"form":form, "action":"Editar"}
    return render(request, 'core/formulas/dietas.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def eliminarCalculoDieta(request, dieta_id):
    dieta = Dieta.objects.get(id=dieta_id)
    dieta.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect('lista_dieta')


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

@login_required(login_url='login')
@admin_only
def calendario(request):
    context = {}
    lista_citas = Appointment.objects.all()
    context = {'lista_citas':lista_citas}
    return render(request, 'core/calendario.html', context)

@login_required(login_url='login')
@admin_only
def historial_calendario(request):
    context = {}
    lista_citas = Appointment.objects.all()
    context = {'lista_citas':lista_citas}
    return render(request, 'core/historial_calendario.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def eliminarCita(request, cita_id):
    cita = Appointment.objects.get(id=cita_id)
    cita.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect('historial-calendario')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin']) 
def get_info_cita(request, cita_id):
    cita = get_object_or_404(Appointment, id=cita_id)
    data = {
        "first_name": cita.client.first_name,
        "last_name": cita.client.last_name,
        "last_name_m": cita.client.profile.last_name_m,
        "date": cita.date,
        "hour": cita.hour,
        "email": cita.client.email,
        "phone": cita.client.profile.phone,
        "commentary":cita.commentary,
    }
    return JsonResponse(data, status=200)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def eliminarCalculoPesoCorregido(request, pesocorregido_id):
    corrected_weight = PesoCorregido.objects.get(id=pesocorregido_id)
    corrected_weight.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect('lista_pesocorregido')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def eliminarCalculoGer(request, ger_id):
    ger = GER.objects.get(id=ger_id)
    ger.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect('lista_ger')

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def eliminarCalculoGrupoNutri(request, grupo_id):
    grupo = Food_Group.objects.get(id=grupo_id)
    grupo.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect('lista_grupo_nutricional')