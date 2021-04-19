from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only

from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def citas(request):
    clientes = User.objects.all()
    context = {'clientes':clientes}
    return render(request, 'citas/prueba.html', context)