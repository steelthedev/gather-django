from django.contrib import admin
from .models import Message, Room,Outline, RoomMember



admin.site.register(Room)
admin.site.register(Outline)
admin.site.register(Message)
admin.site.register(RoomMember)
