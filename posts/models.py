from django.db import models
from django.contrib.auth.models import User
from userApps.models import UserInformation
import os

# Create your models here.
def userApps_media_path(instance, filename):
    return os.path.join('posts/media/', instance.title, filename)


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null= True, blank=True)
    userName = models.ForeignKey(UserInformation, on_delete=models.CASCADE, related_name='infos', null= True, blank=True)
    image= models.ImageField(upload_to= userApps_media_path, default=None, null=True)
    def __str__(self):
        return self.title