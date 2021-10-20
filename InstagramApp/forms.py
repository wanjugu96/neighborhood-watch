from django import forms
from .models import *

class uploadimage(forms.ModelForm):
    name = forms.CharField()
    image = forms.ImageField()
    caption= forms.CharField()
    
    

    class Meta:
        model=Image
        fields=['name','image','caption',]

class createProfileform(forms.ModelForm):
    
    profile_photo = forms.ImageField()
    bio= forms.CharField()

    class Meta:
        model=Profile
        fields=['profile_photo','bio']