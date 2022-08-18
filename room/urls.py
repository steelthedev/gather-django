
from django.urls import path
from . import views

app_name = "room"

urlpatterns = [
    path('lobby/',views.lobby, name="lobby"),
    path('main-room/',views.room, name="meeting"),
    path("get-token/",views.getToken, name="get_token"),
    path('create-member/', views.createMember, name="create_member"),
    path('get-member/', views.getMember, name="get_member"),
    path('delete-member/',views.deleteMember, name="delete_member")
]