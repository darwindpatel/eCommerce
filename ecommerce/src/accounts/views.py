from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
# Create your views here.
def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form" : form
	}
	print("User logged in")
	#print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			#print(request.user.is_authenticated())
			login(request, user)
			#context['form'] = LoginForn()
			return redirect("/")
		else:
			print("Error")
	return render(request, "accounts/login.html", context)

#User = get_user_model
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form" : form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
	return render(request, "accounts/register.html", context)