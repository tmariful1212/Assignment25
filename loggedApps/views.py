from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

from django.contrib.auth import login , logout, authenticate
from django.contrib import messages


# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # set staff status to True
            user.is_staff = True
            user.save()
            login(request, user)
            return redirect('addInfo')
    else:
        form = UserRegistrationForm()
    return render(request, "loggedApps/signup.html", {"form": form})

def userLogout(request):
    logout(request)
    return redirect('login')

def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("profile")  # Redirect to a profile/dashboard page
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "loggedApps/login.html")  # Make sure ⁠ login.html ⁠ exists in your templates folder.