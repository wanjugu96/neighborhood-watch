from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from InstagramApp.forms import uploadimage ,createProfileform
from InstagramApp.models import Image, Profile
from .email import *

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    
    current_user = request.user
    name=current_user.username
    theprofile=Profile(name=name)
    theprofile.save()

    if request.method=='POST':
        form=uploadimage(request.POST,request.FILES)
        if form.is_valid():

            form.save()
    
        else:
                       
            form=uploadimage()
            message=f"Successfully uploaded"

    form=uploadimage()
   
    return render(request,'index.html',{"current_user":current_user,"form":form})


def success(request):
    return HttpResponse('successfully uploaded')

def createProfile(request):
    current_user = request.user
    name=current_user.username
    theprofile=Profile(name=name)
    theprofile.save()

    if request.method=='POST':
        form= createProfileform(request.POST,request.FILES)
        if form.is_valid():

            form.save()
        else:
                       
            form=createProfileform()

    form= createProfileform()
       

    return render(request,'createProfile.html',{"form":form, "current_user":current_user})    