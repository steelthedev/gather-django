from django.db import models






class Room(models.Model):
    name = models.CharField(max_length=300)
    owner = models.ForeignKey("accounts.CustomUser", related_name="profile", on_delete=models.CASCADE)
    duration = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name



class Outline(models.Model):
    title = models.CharField(max_length=500)
    room = models.ForeignKey(Room, related_name="meeting", on_delete=models.CASCADE)
    created_on = models.DateTimeField