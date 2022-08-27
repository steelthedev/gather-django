import email
from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.contrib import messages
from room.models import Room



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

@login_required(login_url="accounts:login")
def CreateMeeting(request):
    if request.user.is_authenticated:
        user=request.user

        try:
            room =  Room.objects.filter(owner=user)
        except:
            pass
        if request.method == "POST":
            name = request.POST["name"].upper()
            start_time=request.POST["start"]
            end_time=request.POST["end"]
            Room.objects.create(name=name,owner=user,start_time=start_time,duration=end_time)
        context ={
            'room':room
        }
        return render(request,'dashboard/create-meeting.html',context)

@login_required(login_url="accounts:login")
def DeleteMeeting(request,id):
    try:
        room=Room.objects.get(pk=id)
    except:
        messages.warning(request,"Meeting could not be found")
        return redirect("dashboard:create_meeting")

    room.delete()
    messages.success(request,"Meeting deleted successfully")
    return redirect("dashboard:create_meeting")
