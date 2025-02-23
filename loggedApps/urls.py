from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView , LoginView

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.userLogout, name='logout'),
  
]