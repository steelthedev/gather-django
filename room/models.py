from django.db import models






class Room(models.Model):
    name = models.CharField(max_length=300)
    owner = models.ForeignKey("accounts.CustomUser", related_name="profile", on_delete=models.CASCADE)
    duration = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=200)
    token = models.CharField(max_length=700)
    


    def __str__(self) -> str:
        return self.name

class RoomMember(models.Model):
    name = models.CharField(max_length=300)
    room_name = models.CharField(max_length=300)
    uid = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.name
    



class Outline(models.Model):
    title = models.CharField(max_length=500)
    room = models.ForeignKey(Room, related_name="meeting", on_delete=models.CASCADE)
    created_on = models.DateTimeField



class Message(models.Model):
    member = models.CharField(max_length=200)
    content = models.TextField()
    room = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.member

    class Meta:
        ordering = ('created_on',)