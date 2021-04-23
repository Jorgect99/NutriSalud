from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only
from .forms import AppointmentForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def setAppointment(request):
    form = AppointmentForm()
    context = {}
    if request.POST:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user
            appointment.save()
            request.user.profile.phone = request.POST.get('phone')
            request.user.profile.save()
            return HttpResponseRedirect('/web')
    context['form'] = form

    return render(request, 'citas/citas.html', context)