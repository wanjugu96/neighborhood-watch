from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from InstagramApp.forms import uploadimageform ,createProfileform
from InstagramApp.models import Image, Profile
from .email import *

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    
    current_user = request.user
    username=current_user.username


    aprofile=Profile(name=username)
    aprofile.save()
              

    #return render(request,'index.html',{"current_user":current_user,})
    return HttpResponseRedirect('uploadimage')


def success(request):
    return HttpResponse('successfully uploaded')

def uploadimage(request):
    current_user = request.user
    username=current_user.username
    #request.FILES)

    if request.method=='POST':
        form=uploadimageform(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            image=form.cleaned_data['image']
            caption=form.cleaned_data['caption']

            profile=Profile.objects.get(name=username)
            profile_id=profile.id


            theimage=Image(name=name,image=image,caption=caption,profile_id=profile_id)
            theimage.save()

            #form.save()
    
        else:
            form=uploadimageform()
            message=f"Successfully uploaded"

    form=uploadimageform()
    profile=Profile.objects.filter(name=username)           

    return render(request,'index.html',{"current_user":current_user,"form":form,"profile":profile})

def createProfile(request):
    current_user = request.user
    username=current_user.username
    

    if request.method=='POST':
        form= createProfileform(request.POST,request.FILES)
        if form.is_valid():
            bio=form.cleaned_data['bio']
            profile_photo=form.cleaned_data['profile_photo']
            profile=Profile.objects.get(name=username)
            profile.bio=bio
            profile.profile_photo=profile_photo
          
            #theprofile=Profile(profile_photo=profile_photo,bio=bio)
            profile.save()

            return redirect('profile', name=username)


            #form.save()
        else:
                       
            form=createProfileform()

    form= createProfileform()
       

    return render(request,'createProfile.html',{"form":form, "current_user":current_user})


def profile(request,name):
        profile=Profile.objects.get(name=name) 

        return render(request ,'profile.html',{"profile":profile})           
    


    