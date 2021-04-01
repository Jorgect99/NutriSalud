from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index-dashboard.html')

def clientes(request):
    return render(request, 'core/clientes.html')

def imc(request):
    return render(request, 'core/formulas/imc.html')
    
def met(request):
    return render(request, 'core/formulas/met.html')

