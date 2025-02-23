from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView , LoginView

urlpatterns = [
    path('create/', views.createPost, name='createPost'),
    path('edit/<int:pk>/', views.editPost, name='editPost'),
    path('delate/<int:pk>/', views.deletePost, name='deletePost'),
  
]