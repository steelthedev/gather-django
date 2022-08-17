
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout

def Signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if name and email and password and password2:

            if not password == password2:
                messages.warning(request,"Passwords does not match")
                return redirect("accounts:signup")

            CustomUser.objects.create(full_name = name, email = email, password = make_password(password))
            messages.success(request, "Registration successful")
            return redirect("accounts:login")

    return render(request,'accounts/signup.html')


def Signin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard:dashboard")
        return redirect("accounts:login")
    return render(request,'accounts/login.html')

def Signout(request):
    
    logout(request)
    return redirect("accounts:login")

