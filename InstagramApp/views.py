from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from InstagramApp.forms import uploadimage ,createProfileform
from InstagramApp.models import Image, Profile
from .email import *

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    
    current_user = request.user
    username=current_user.username
    

    if request.method=='POST':
        form=uploadimage(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            image=form.cleaned_data['image']
            caption=form.cleaned_data['caption']
            profile=Profile.objects.filter(name=username)
            # profile_id=profile.id
            # theimage=Image(name=name,image=image,caption=caption,profile_id=profile_id)
            # theimage.save()

            #form.save()
    
        else:
                       
            form=uploadimage()
            message=f"Successfully uploaded"

    form=uploadimage()
   
    return render(request,'index.html',{"current_user":current_user,"form":form,"profile":profile})


def success(request):
    return HttpResponse('successfully uploaded')

def createProfile(request):
    current_user = request.user
    name=current_user.username
    

    if request.method=='POST':
        form= createProfileform(request.POST,request.FILES)
        if form.is_valid():
            bio=form.cleaned_data['bio']
            profile_photo=form.cleaned_data['profile_photo']
            theprofile=Profile(name=name,profile_photo=profile_photo,bio=bio)
            theprofile.save()

            #form.save()
        else:
                       
            form=createProfileform()

    form= createProfileform()
       

    return render(request,'createProfile.html',{"form":form, "current_user":current_user})    