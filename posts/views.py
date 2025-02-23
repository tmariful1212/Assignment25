from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from userApps.models import UserInformation
from django.contrib.auth.decorators import login_required
from .forms import  PostForm
from .import forms
from django.contrib.auth import login
from .models import Post
from django.contrib import messages

# Create your views here.
@login_required
def createPost(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.userName = UserInformation.objects.get(user=request.user)
            post.save()
            messages.success(request, "Post Create successfully .")
            return redirect('profile')
    else:
        form = PostForm()
    info= UserInformation.objects.get(user=request.user)
    return render(request, "posts/createPost.html", {"form": form, "info":info})

@login_required
def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES, instance=post) 
        if form.is_valid():
            form.save()
            messages.success(request, "Post Updated successfully .")
            return redirect('profile')
    else:
        form = PostForm(instance=post)
    info= UserInformation.objects.get(user=request.user)
    return render(request, "posts/createPost.html", {"form": form, "info":info})

@login_required
def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post Deleted successfully .")
    return redirect('profile')