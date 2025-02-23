from django.contrib.auth.models import User
from django.db import models
import os

# Create your models here.
def userApps_media_path(instance, filename):
    return os.path.join('userApps/media/', instance.fullName, filename)
# Create your models here.

class UserInformation(models.Model):
    fullName = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=50)
    image= models.ImageField(upload_to=userApps_media_path, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addInfo', null= True, blank=True)
    def __str__(self):
       return f"{self.fullName}"