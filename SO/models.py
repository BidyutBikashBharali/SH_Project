from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserData(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	fullname =  models.CharField(max_length=100, null=False)
	address = models.CharField(max_length=100, null=False)
	date_created = models.DateTimeField(auto_now_add=True, null=False)

	
    

class UserPost(models.Model):
	title = models.CharField(max_length=200, null=False)
	tag = models.CharField(max_length=100, null=False)
	url = models.URLField(max_length = 200, null=True, blank=True)
	description = models.TextField(null=False)
	date_created = models.DateTimeField(auto_now_add=True, null=False)
	user = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE) 
    
    