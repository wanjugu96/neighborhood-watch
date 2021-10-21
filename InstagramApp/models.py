from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='InstaImages',blank=True,null=True,default='')
    bio=models.TextField(blank=True,null=True)
    name=models.CharField(max_length=30,default='default name',unique=True)

    @classmethod
    def search_name(cls,search_term):
        profiles=cls.objects.filter(name__icontains=search_term)  
        return profiles 
       
   

class Image(models.Model):
    image=models.ImageField(upload_to='InstaImages')
    name = models.CharField(max_length=30)
    caption=models.TextField()
    profile=models.ForeignKey(Profile,on_delete=models.PROTECT,null=True)
    likes=models.IntegerField(null=True,default=0)




class Comment(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.PROTECT)
    comment=models.TextField()
    image=models.ForeignKey(Image,on_delete=models.PROTECT,blank=True,null=True,default='')
        





