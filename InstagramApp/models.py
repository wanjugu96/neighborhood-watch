from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='InstaImages')
    bio=models.TextField()

class Image(models.Model):
    image=models.ImageField(upload_to='InstaImages')
    name = models.CharField(max_length=30)
    caption=models.TextField()
    profile=models.ForeignKey(Profile,on_delete=models.PROTECT)
    likes=models.IntegerField()
    comments=models.TextField()


class Comment(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.PROTECT)
    comment=models.TextField()
    



