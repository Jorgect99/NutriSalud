from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('clientes', views.clientes, name="clientes"),
    path('formula/imc', views.imc, name="imc"),
    path('formula/met', views.met, name="met"),
]