from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
 path('profile/', views.profile, name= 'profile'),
 path('home/', views.homepage, name='homepage'),
 path('info/', views.addUserInformation, name='addInfo'),
]
