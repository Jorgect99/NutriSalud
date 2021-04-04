from django.urls import path
from . import views

urlpatterns = [
    #paths accounts
    path('registration/', views.registerPage, name='registration'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
]