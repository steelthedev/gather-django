import email
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.contrib import messages

@login_required(login_url="accounts:login")
def Dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required(login_url="accounts:login")
def changePersonalDetails(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]

        user = request.user

        user.full_name = name
        user.email = email
        user.save()
        messages.success(request,"Update successfull")
        return redirect("dashboard:dashboard")
    
    messages.warning(request,"something went wrong")
    return redirect("dashboad:dashboard")

@login_required(login_url="accounts:login")
def UpdateContact(request):
    if request.method == "POST":
        user = request.user
        phone = request.POST["phone"]
        language = request.POST["language"]
        time_zone = request.POST["timezone"]

        user.phone_number = phone
        user.language = language
        user.time_zone = time_zone
        user.save()
        messages.success(request,"Update successfull")
        return redirect("dashboard:dashboard")
    
    messages.warning(request,"something went wrong")
    return redirect("dashboad:dashboard")
