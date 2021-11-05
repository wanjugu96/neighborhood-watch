from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email

from InstagramApp.forms import commentform, updatecaption, uploadimageform ,createProfileform
from InstagramApp.models import Rate, Image, Profile
from .email import *

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    
    current_user = request.user
    username=current_user.username
    email=current_user.email

    #send_welcome_email(username,email)

    thisprofile=Profile.objects.filter(name = username)
    if thisprofile:
        return redirect('profile', username)
    else:
        aprofile=Profile(name=username)
        aprofile.save()

        email=current_user.email

        #send_welcome_email(username,email)

              

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
            Businessimage=form.cleaned_data['Businessimage']
            description=form.cleaned_data['description']
            link='xxxx'

            profile=Profile.objects.get(name=username)
            profile_id=profile.id


            theimage=Image(name=name,Businessimage=Businessimage,description=description,profile_id=profile_id,link=link)
            theimage.save()

            return redirect('profile', name=username)


            #form.save()
    
        else:
            form=uploadimageform()
            message=f"Successfully uploaded"

    form=uploadimageform()
    profile=Profile.objects.filter(name=username)

    profiles=Profile.objects.filter()           

    return render(request,'index.html',{"current_user":current_user,"form":form,"profile":profile,"profiles":profiles})

def createProfile(request):
    current_user = request.user
    username=current_user.username
    

    if request.method=='POST':
        form= createProfileform(request.POST,request.FILES)
        if form.is_valid():
            bio=form.cleaned_data['bio']
            Phone_num=form.cleaned_data['Phone_num']
            email=form.cleaned_data['email']
            profile_photo=form.cleaned_data['profile_photo']
            profile=Profile.objects.get(name=username)
            profile.bio=bio
            profile.profile_photo=profile_photo
            profile.email=email
            profile.Phone_num=Phone_num
          
            #theprofile=Profile(profile_photo=profile_photo,bio=bio)
            profile.save()

            return redirect('profile', name=username )


            #form.save()
        else:
                       
            form=createProfileform()

    form= createProfileform()
    profile=Profile.objects.get(name=username)
       

    return render(request,'createProfile.html',{"form":form, "current_user":current_user, "profile":profile})


def profile(request,name):
    current_user = request.user
    username=current_user.username
    profile=Profile.objects.get(name=name)

    id=profile.id 

    
    

    Allimages=Image.objects.filter(profile_id = id)
    form=uploadimageform()

    

    return render(request ,'profile.html',{"profile":profile, "Allimages":Allimages,"form":form,"current_user":current_user}) 

def updatelikes(request,id):
    image=Image.objects.get(id = id)

    count=image.likes + 1 
    Image.objects.filter(id = id).update(likes=count)

    return render(request,'singleimage.html',{"image":image})

def singleimage(request,id):

    current_user=request.user
    username=current_user.username
    image=Image.objects.get(id = id)

    if request.method=='POST':
        form= commentform(request.POST,request.FILES)
        if form.is_valid():
            design=form.cleaned_data['design']
            usability=form.cleaned_data['design']
            content=form.cleaned_data['content']
            
            profile=Profile.objects.get(name=username)
            profile_id=profile.id
            total=(design+usability+content)/3
            commentobj=Rate(content=content,profile_id=profile_id,image_id=id,usability=usability,design=design,total=total)

            commentobj.save()

            total=(design+usability+content)/3

            
            return redirect('singleimage', id)
    else:
                    
        form=commentform()



    form= commentform()
    #total=(design+usability+content)/3

    rates=Rate.objects.filter(image_id=id)
    
    


    return render(request,'singleimage.html',{"image":image, "form":form,"rates":rates})

def deleteimage(id):
    Image.objects.filter(id=id).delete()
    message=f"Successfully deleted"

    #return redirect('singleimage',id ,{"message":message})
    return HttpResponseRedirect('successfully deleted')

    #return redirect('singleimage',id ,{"message":message})

def search_name(request):
    if 'name' in request.GET and  request.GET["name"]:
        search_term=request.GET.get("name")
        profiles=Profile.search_name(search_term)
        message=f"{search_term}"
        message=f"{search_term}"
        return render(request, 'search.html',{"message":message,"profiles": profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})   


    




    
    


    