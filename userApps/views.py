from django.contrib.auth.models import User
from django.contrib import messages
from userApps.models import UserInformation
from .import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth import login
from django.db.models import Q

@login_required
def profile(request):
    user= request.user
    post= Post.objects.filter(user=request.user).order_by("-created_at")

    date_order = request.GET.get('date')
    if date_order == 'newest':
        post = post.order_by('-created_at')
    elif date_order == 'oldest':
        post = post.order_by('created_at')
    
    # Filter by media type
    media = request.GET.get('media')
    if media == 'images':
        post = post.filter(Q(image__isnull=False)& ~Q(image=''))
    elif media == 'text':
        post = post.filter(Q(image__isnull=True)|Q(image=''))

    info= UserInformation.objects.get(user=request.user)
    context={
        'user': user,
        'posts': post,
        'info': info 
    }
    print(context)
    return render(request, 'userApps/profile.html', context )

@login_required
def homepage(request):
    user= request.user
    post= Post.objects.all()

   

    date_order = request.GET.get('date')
    if date_order == 'newest':
        post = post.order_by('-created_at')
    elif date_order == 'oldest':
        post = post.order_by('created_at')
    
    # Filter by media type
    media = request.GET.get('media')
    if media == 'images':
        post = post.filter(Q(image__isnull=False)& ~Q(image=''))
    elif media == 'text':
        post = post.filter(Q(image__isnull=True)|Q(image=''))
    
    # Filter by author (username)
    author = request.GET.get('author')
    
    if author:
        author_obj = get_object_or_404(UserInformation, fullName=author)
        post = Post.objects.filter(userName=author_obj)
    
    # Keyword search in post content
    query = request.GET.get('q')
    if query:
        post = post.filter(Q(title__icontains=query))


    info= UserInformation.objects.get(user=request.user)
    context={
        'user': user,
        'posts': post,
        'info': info
    }
    return render(request, 'userApps/homepage.html', context )



@login_required
def addUserInformation(request):
    if request.method == 'POST':
       form=forms.UserInformationForm(request.POST, request.FILES)
       if form.is_valid():
            
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, "Information Added Successfully !!!!")
            return redirect('profile') 
       else:
            messages.add_message(request, messages.ERROR, "Please Enter Valid Data !!!!")
            form=forms.UserInformationForm(request.POST, request.FILES)
            return render(request, 'userApps/addUserInformation.html', {'form':form, 'update':True})
    else:
        form=forms.UserInformationForm()
        return render(request, 'userApps/addUserInformation.html', {'form':form})



