from django.db import models
# Create your models here.py m  m


class Users(models.Model):
    username=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    img=models.ImageField(upload_to='img')
    number=models.CharField(max_length=14)
    is_admin=models.BooleanField(default=False)
   
