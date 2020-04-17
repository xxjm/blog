from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def zhuce(request):
	return render(request, 'account/zhuce.html')

def login(request):
	if request.method == "POST":
		user = auth.authenticate(request, username=request.POST['用户名'], password=request.POST['密码'])
		if user is None:
			return render(request, 'account/login.html', {'错误':'用户名不存在'})
		else:
			auth.login(request, user)	
			return redirect("account:页面")
	else:
		return render(request,'account/login.html')

def logout(request):
	auth.logout(request)
	return redirect("account:页面")

def signin(request):
	if request.method == 'POST':
		注册表单=UserCreationForm(request.POST)
		if 注册表单.is_valid():
			注册表单.save()
			user = auth.authenticate(request, username=注册表单.cleaned_data['username'], password=注册表单.cleaned_data['password1'])
			auth.login(request, user)
			return redirect("account:页面")
	else:
		注册表单=UserCreationForm()
	
	content ={'注册表单':注册表单}
	return render(request,'account/signin.html',content)
