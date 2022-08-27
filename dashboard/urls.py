from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns = [
    path('', views.Dashboard, name="dashboard"),
    path('update/name/',views.changePersonalDetails, name="update_name"),
    path('update-contact/',views.UpdateContact, name="update_contact"),
    path('create-meeting/',views.CreateMeeting, name="create_meeting")
]