from django import forms
from .models import *

class uploadimageform(forms.ModelForm):
    name = forms.CharField()
    image = forms.ImageField()
    caption= forms.Textarea()
    
    

    class Meta:
        model=Image
        fields=['name','image','caption',]

class createProfileform(forms.ModelForm):
    
    profile_photo = forms.ImageField()
    bio= forms.Textarea()

    class Meta:
        model=Profile
        fields=['profile_photo','bio']