import json
from accounts.models import CustomUser
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room,Outline,Message



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = 'chat_%s' % self.room_name

        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )


    async def disconnect(self,code):
        return await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
    )


    async def receive(self,text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_messages(username,room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'room':room,
            }
        )

    async def chat_message(self,event):
        message = event['message']
        username = event['username']
       

        await self.send(text_data =json.dumps({
            'message':message,
            'username':username
        }))

    @sync_to_async
    def save_messages(self,username,room,message):
        user = CustomUser.objects.get(username = username)
        room = Room.objects.get(pk=room)

        Message.objects.create(user = user, room = room, content = message)
        
        


