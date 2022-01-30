from django.db import models
from django import forms
import uuid
# Create your models here.

class User(models.Model):

	username = models.CharField(max_length=300,null=True,blank=True,unique=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

class Credential(models.Model):
	user = models.ForeignKey('User',on_delete=models.CASCADE,null=True)
	service = models.CharField(max_length=300,null=True,blank=False)
	username = models.CharField(max_length=300,null=True,blank=True,default="")
	email = models.EmailField(null=True,blank=True,default="")
	password = models.CharField(max_length=300,null=True,blank=False,default='')
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)



