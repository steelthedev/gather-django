from django.contrib import admin
from .models import Message, Room,Outline, RoomMember
from django.contrib.sessions.models import Session,SessionManager


admin.site.register(Room)
admin.site.register(Outline)
admin.site.register(Message)
admin.site.register(RoomMember)
admin.site.register(Session)
