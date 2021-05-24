from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only
from .forms import AppointmentForm
from django.contrib.auth.models import User
from .models import Appointment

# Create your views here.
@login_required(login_url='login')
def setAppointment(request):
    form = AppointmentForm()
    context = {}
    if request.POST:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return HttpResponseRedirect('/web')

    lista_citas = Appointment.objects.all()
    context = {'form':form ,'lista_citas':lista_citas}

    return render(request, 'citas/citas.html', context)