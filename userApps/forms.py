from django import forms
from .import models

class UserInformationForm(forms.ModelForm):
    class Meta:
          model=models.UserInformation
          exclude= ['user']
          fields='__all__'
          labels={
                 'name': 'Full Name',
                'image': 'Profile Picture',

    }
          help_texts={
                 'name': 'Enter your full name',
                'image': 'Upload your profile picture',
    }
    