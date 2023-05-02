from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,BaseUserManager,User

# Create your models here.py m  m
from django.contrib.auth.hashers import make_password

class Myusermanager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        
        if not username:
            raise ValueError("sayname yazin")
 
        user = self.model(username=username,**extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, username, password,**extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username,  password, **extra_fields)

    def create_superuser(self, username,  password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)

class Myuser(AbstractBaseUser):
    last_login=None
    name=models.CharField(max_length=20,blank=True,default='')
    surname=models.CharField(max_length=20,blank=True,default='')
    email=models.EmailField(blank=True,default='')
    username=models.CharField(max_length=20,unique=True)
    number=models.CharField(max_length=14,blank=True,null=True)
    img=models.ImageField(blank=True,null=True,default='',upload_to='img')
    # birth=models.DateField()
    password=models.CharField(max_length=255)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=Myusermanager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return True

    
    def has_module_perms(self, module):
        return True

    def __str__(self) -> str:
        return self.username
    
    def save(self,*args,**kwargs):
        self.password=make_password(self.password)
        super(Myuser,self).save(*args,**kwargs)

class Categories(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
class Products(models.Model):
    title=models.CharField(max_length=20)
    text=models.TextField()
    category=models.ForeignKey('Categories',on_delete=models.CASCADE)



   
