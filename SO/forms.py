from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({ 'name':'username', 'style':'width:75%;', 'class':'w3-input', 'placeholder':'Set An Unique User Name'})
		self.fields['email'].widget.attrs.update({ 'name':'email', 'style':'width:75%;', 'class':'w3-input', 'placeholder':'Enter Your Email'})
		self.fields['password1'].widget.attrs.update({ 'name':'password1', 'style':'width:75%;', 'class':'w3-input', 'placeholder':'Set A Password'})
		self.fields['password2'].widget.attrs.update({ 'name':'password2', 'style':'width:75%;', 'class':'w3-input', 'placeholder':'Set A Password'})
		


class UserDataForm(ModelForm):
	class Meta:
		model = UserData
		fields = '__all__'
		exclude = ['user', 'date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['fullname'].widget.attrs.update({ 'name':'fullname', 'style':'width:75%;', 'class':'w3-input', 'placeholder':'Enter Your Full Name'})
		self.fields['address'].widget.attrs.update({ 'name':'address', 'style':'width:75%;', 'class':'w3-input', 'placeholder':'Enter Your Address'})
		



class UserPostForm(ModelForm):
	class Meta:
		model = UserPost
		fields = '__all__'
		exclude = ['date_created', 'user_data', 'color']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({ 'name':'title', 'style':'width:75%;', 'class':'w3-input', 'placeholder':'Enter Title' })
		self.fields['tag'].widget.attrs.update({ 'name':'tag', 'style':'width:75%;', 'class':'w3-input', 'placeholder':"Give a Tag( Eg: '#Jobs', '#Internship', '#Content-Writing', '#AI/ML', '#JAVA' etc ) ", 'pattern':'#.*' })
		self.fields['url'].widget.attrs.update({ 'name':'url', 'style':'width:75%;', 'class':'w3-input', 'placeholder':'Enter URL ( Optional ) ', 'pattern':'https://.*' })
		self.fields['description'].widget.attrs.update({ 'name':'description', 'style':'width:75%; resize:none;', 'class':'w3-round-large', 'placeholder':'   Description  ' })
		