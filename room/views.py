from django.shortcuts import render,redirect
from agora_token_builder import RtcTokenBuilder
import random
import time
from django.http import JsonResponse
from .models import RoomMember,Room,Message
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

def lobby(request):

    return render(request,'room/lobby.html')


def getToken(request):
    appId = "426e57ec84fa41bd8172c0d247994c59"
    appCertificate = "a2b5aa04ba424716ab897b82bd3566a6"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 *24
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    
    try:
        room_db_check = Room.objects.get(uid=channelName)
        if room_db_check:
            token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
            return JsonResponse({'token': token, 'uid': uid}, safe=False)
    except ObjectDoesNotExist:
        return JsonResponse({'error':'Room does not exist'}, safe=False)



def room(request):
    
    room = request.GET.get("room")
    try:
        meeting = Room.objects.get(uid=room)
    except ObjectDoesNotExist:
        messages.info(request,'Room name must be valid')
        return redirect('room:lobby')
    message = Message.objects.filter(room=meeting.id)
    context ={
        "messages":message,
        "room":meeting,
    }
    return render(request,'room/room.html', context)




@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
   
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':name}, safe=False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    print(member.name)
    print(member.uid)
    print(member.room_name)
    member.delete()
    return JsonResponse('Member has been deleted', safe=False)


def meetingDetails(request):
    uid = request.GET.get('room')
    try:
        room= Room.objects.get(
            uid=uid,
        )
        return JsonResponse({'name':room.name,'start':room.start_time,'end':room.duration,'owner':room.owner.email}, safe=False)
    except:
        return JsonResponse({'error':'Room does not exist'}, safe=False)

    