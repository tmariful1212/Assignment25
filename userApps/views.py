
from django.contrib import messages
from userApps.models import UserInformation
from .import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth import login 

@login_required
def profile(request):
    user= request.user
    post= Post.objects.filter(user=request.user).order_by("-created_at")
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
    post= Post.objects.all().order_by("-created_at")
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



# def update_teacher(request, id):  
#     teacher=models.Teacher.objects.get(id=id)
    
#     if request.method == 'POST':
#         form=forms.TeacherForm(request.POST, request.FILES, instance=teacher)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Teacher Updated Successfully !!!!")
#             return redirect('teacher_home')
        
#         else:
#             messages.add_message(request, messages.ERROR, "Please Enter Valid Data !!!!")
#             form=forms.TeacherForm(request.POST, request.FILES, instance=teacher)
#             return render(request, 'teacher/teacher_create.html', {'form':form, 'update':True})
    
#     else:
#         form=forms.TeacherForm(instance=teacher)
#         return render(request, 'teacher/teacher_create.html', {'form':form, 'update':True})
    
    




# def delete_teacher(request, id):
#     teacher= models.Teacher.objects.get(id=id)
#     teacher.delete()
#     messages.add_message(request, messages.SUCCESS, "Teacher Deleted Successfully !!!!")
#     return redirect('teacher_home')