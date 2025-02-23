from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse



# Create your views here.


def home(request):
    # teachers=models.Teacher.objects.all()
    context={}
    return render(request, 'loggedApps/welcome.html' , context)