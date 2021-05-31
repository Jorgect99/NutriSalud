from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="admindashboard"),
    path('clientes', views.clientes, name="clientes"),
    path('clientes/delete/<int:cliente_id>', views.eliminarCliente, name="eliminar_cliente"),
    
    path('formula/imc', views.imc, name="imc"),
    path('formula/pesocorregido', views.pesoCorregido, name="pesocorregido"),
    path('formula/ger', views.ger, name="ger"),

    path('formula/lista-imc', views.lista_imc, name="lista_imc"),
    path('formula/lista-imc/delete/<int:imc_id>', views.eliminarCalculoIMC, name="eliminar_calculo_imc"),
    path('formula/lista-pesocorregido', views.lista_pesocorregido, name="lista_pesocorregido"),
    path('formula/lista-pesocorregido/delete/<int:pesocorregido_id>', views.eliminarCalculoPesoCorregido, name="eliminar_calculo_pesocorregido"),
    path('formula/lista-ger', views.lista_ger, name="lista_ger"),
    path('formula/lista-ger/delete/<int:ger_id>', views.eliminarCalculoGer, name="eliminar_calculo_ger"),
    path('formula/lista-dieta', views.lista_dieta, name="lista_dieta"),
    path('formula/lista-dieta/delete/<int:dieta_id>', views.eliminarCalculoDieta, name="eliminar_calculo_dieta"),
    path('formula/lista-dieta/edit/<int:dieta_id>', views.editarCalculoDieta, name="editar_calculo_dieta"),

    path('formula/grupos-nutri', views.gruposNutricionales, name="grupos-nutri"),
    path('formula/lista-grupos-nutri', views.lista_gruposNutricionales, name="lista_grupo_nutricional"),
    path('formula/lista-grupos-nutri/delete/<int:grupo_id>', views.eliminarCalculoGrupoNutri, name="eliminar_calculo_grupo"),
    path('formula/menu', views.menu, name="menu"),
    path('formula/dieta', views.dieta, name="dieta"),


    path('calendario/', views.calendario, name="calendario"),
]
