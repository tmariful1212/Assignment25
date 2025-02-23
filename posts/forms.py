from django import forms
from .import models

class PostForm(forms.ModelForm):
    class Meta:
          model=models.Post
          exclude= ['user','userName']
          fields='__all__'
          labels={
                 'title': 'Title',
                'image': 'Picture',

    }
          help_texts={
                 'name': 'Enter your full name',
                'image': 'Upload your profile picture',
    }
    