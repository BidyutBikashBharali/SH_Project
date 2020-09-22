from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .models import UserData, UserPost
from .forms import UserForm, UserDataForm, UserPostForm
import random
# Create your views here.

def SI(request):
	print(request.user.is_authenticated)
	if request.user.is_authenticated:
		return redirect('Profile')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('pass')
		
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Signed In Successfully:)") 
			return redirect('SUD') 
		else:
			messages.error(request, "No such user with the submited credential exist!")
			return redirect('SignIn')   

	return render(request, 'SI.html')



def SU(request):
	form = UserForm()
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1') 

			if User.objects.filter(username=username).exists():
				messages.warning(request, "Username already exist! Try something unique.")
				return redirect("SignUp") 
			form.save()
			
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, f"Signed Up Successfully with Username '{username}' :)")

			return redirect('SUD') 
	return render(request, 'SU.html', {'form':form})




def LO(request):
	logout(request)
	messages.success(request, "Loged Out Successfully:)") 
	return redirect('SignIn')


@login_required(login_url='SignIn')
def SetUserData(request):
	try:
		if request.user.userdata.fullname is not None or request.user.userdata.address is not None:
			return redirect('Profile')
	except:
		form = UserDataForm()
		if request.method == 'POST':
			form = UserDataForm(request.POST)
			if form.is_valid():
			    ud = UserData(fullname=form.cleaned_data.get('fullname'), address=form.cleaned_data.get('address'), user=request.user)
			    ud.save()
			    return redirect('Profile')
		return render(request, 'SUD.html', {"form":form})


@login_required(login_url='SignIn')
def Profile(request):
	try:
		ud = request.user.userdata    
		up = ud.userpost_set.all()
		return render(request, 'Profile.html', {"userdata":ud, "userpost":up})
	except:
		ud = None
		up = None
		return render(request, 'Profile.html', {"userdata":ud, "userpost":up})



@login_required(login_url='SignIn')
def Post(request):
	form = UserPostForm()
	if request.method == 'POST':
		form = UserPostForm(request.POST)
		if form.is_valid():
		    colors = ['w3-border-red', 'w3-border-pink', 'w3-border-purple', 'w3-border-deep-purple', 'w3-border-blue', 'w3-border-aqua', 'w3-border-teal', 'w3-border-lime', 'w3-border-yellow', 'w3-border-amber', 'w3-border-orange', 'w3-border-brown', 'w3-border-gray', 'w3-border-black']
		    color = random.choice(colors)
		    up = UserPost(title=form.cleaned_data.get('title'), tag=form.cleaned_data.get('tag'), url=form.cleaned_data.get('url'), description=form.cleaned_data.get('description'), color=color, user_data=request.user.userdata)
		    up.save()
		    return redirect('Profile')

	return render(request, 'Post.html', {"form":form})




@login_required(login_url='SignIn')
def SearchFeed(request):
	if request.method == 'POST':
		tag = request.POST.get('tag')
		up = UserPost.objects.filter(tag=tag)
		return render(request, 'Feed.html', {"userpost":up})

	up = UserPost.objects.all()
	return render(request, 'Feed.html', {"userpost":up})



