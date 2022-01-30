from django.shortcuts import render,redirect
from .forms import UserForm, CredentialForm
from decouple import config
from .models import User,Credential
from django.contrib import messages
import json
# Create your views here.
def register(request):
	try:
		with open('log.json','r') as env:
			logged = json.load(env)
		if logged['logged'].strip() == "Yes":
			return redirect('index')
	except:
		pass
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'User Registered Successfully!')
			return redirect('login')
		else:
			form = UserForm()
			messages.error(request,'Registeration Failed. Please Try Again')
			return render(request,'pwManager/register.html',context={'form':form})
	else:
		form = UserForm()
		return render(request,'pwManager/register.html',context={'form':form})

def login(request):
	form = UserForm()
	try:
		with open('log.json','r') as env:
			logged = json.load(env)
		if logged['logged'].strip() == "Yes":
			return redirect('index')
	except:
		pass
	if request.method == 'POST':
		username = request.POST['username']
		try:
			user = User.objects.get(username=username)
			with open('log.json','w') as env:
				logged = {'logged':"Yes",'user':username}
				json.dump(logged,env)

			messages.success(request,'Successfully Logged In')
			return redirect('index')

		except Exception as e:
			print(e)
			messages.error(request,'User Does Not Exist')
			return render(request,'pwManager/login.html',context={"form":form})
	else:
		return render(request,'pwManager/login.html',context={"form":form})

def index(request):
	try:
		with open('log.json','r') as env:
			logged = json.load(env)
			print(logged['logged'])
		if logged['logged'].strip() == "Yes":
			credential = Credential.objects.filter( user__username=logged['user'].strip() )
			return render(request,'pwManager/index.html',context={'user':logged['user'],'credential':credential})
		else:
			return redirect('login')


	except Exception as e:
		print(e)
		return redirect('login')

	
# def bio_auth(request):
	

def logout(request):
	try:
		with open('log.json','r') as env:
			logged = json.load(env)
		if logged['logged'] == "Yes":
			with open('log.json','w') as env:
				pass
			return redirect('login')
		else:
			return redirect('login')
	except:
		return redirect('login')


def data_input(request):
	try:
		with open('log.json','r') as env:
			logged = json.load(env)
		if logged['logged'].strip() == "Yes":
			if request.method == "POST":
				form = CredentialForm(request.POST or None)
				if form.is_valid():
					data = form.save()
					data.user = User.objects.get(username=logged['user'].strip())
					data.save()
					messages.success(request,'Submitted Successfully!')
					return redirect('index')
				else:
					form = CredentialForm()
					messages.error(request,'Submission Failed. Please Try Again')
					return render(request,'pwManager/data_input.html',context={'logged':'Yes','form':form})
			else:
				form = CredentialForm()
				return render(request,'pwManager/data_input.html',context={'logged':'Yes','form':form})
		else:
			return redirect('login')
	except Exception as e:
		print(e)
		return redirect('register')

def delete_cred(request, pk):
	credential = Credential.objects.get(id=pk)
	credential.delete()
	return redirect('index')

def edit_cred(request, pk):
	credential = Credential.objects.get(id=pk)
	form = CredentialForm(instance=credential)
	try:
		with open('log.json','r') as env:
			logged = json.load(env)
		if logged['logged'].strip() == "Yes":
			
			if request.method == 'POST':
				form = CredentialForm(request.POST, instance=credential)
				if form.is_valid():
					form.save()
					return redirect('index')
			else:
				return render(request,'pwManager/data_input.html',context={'form':form})
	except:
		messages.error(request,'Some Error Occured!!!')
		return redirect('index')
	