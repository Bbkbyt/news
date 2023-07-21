from django.db import models
from django.contrib.auth.models import User #import user as foreignkey
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=2,choices=(('1','active'),('2','inactive')),default='1')
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

   
class City(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    describtion=RichTextUploadingField()
    banner=models.ImageField(upload_to='news_baner')
    status=models.CharField(max_length=2,choices=(('1','published'),('2','unpublished')),default='2')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.title} writed by {self.user.username}"