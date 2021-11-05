from django import forms
from django.forms.widgets import Textarea
from .models import *

class uploadimageform(forms.ModelForm):
    # title = forms.CharField()
    name = forms.CharField()
    Busines_image = forms.ImageField()
    description= forms.Textarea()
    # link = forms.CharField()

    class Meta:
        model=Image
        fields=['name','Businessimage','description']

class createProfileform(forms.ModelForm):
    
    profile_photo = forms.ImageField()
    bio= forms.Textarea()
    Phone_num=forms.CharField()
    email = forms.CharField()

    class Meta:
        model=Profile
        fields=['profile_photo','bio','Phone_num','email']

class commentform(forms.ModelForm):
    design=forms.IntegerField()
    usability=forms.IntegerField()
    content=forms.IntegerField()



    class Meta:
        model=Rate
        fields=['design','design','content']

        
class  updatecaption(forms.Form):
    caption=forms.CharField(max_length=255)        