from django.db import models

# Create your models here.
class Users(models.Model):
    email=models.CharField(max_length=70,blank=False,default='')
    password=models.CharField(max_length=20,blank=False,default='')
