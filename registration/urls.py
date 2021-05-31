from django.urls import path
from . import views

urlpatterns = [
    #paths accounts
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('profile/', views.profile, name='profile'),
]