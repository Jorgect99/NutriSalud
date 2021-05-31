from django.urls import path, re_path
from . import views

web_patterns = ([
    path('web/', views.home, name="home"),
    path('web/#about', views.home, name="about"),
    path('web/#services', views.home, name="services"),
    path('web/#contact', views.home, name="contact"),
], 'web')