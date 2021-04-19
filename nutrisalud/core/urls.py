from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="admindashboard"),
    path('clientes', views.clientes, name="clientes"),
    path('clientes/delete/<int:cliente_id>', views.eliminarCliente, name="eliminar_cliente"),
    path('formula/imc', views.imc, name="imc"),
    path('formula/met', views.met, name="met"),
]
