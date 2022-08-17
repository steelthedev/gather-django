from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns = [
    path('', views.Dashboard, name="dashboard"),
    path('dashboard/update/name',views.changePersonalDetails, name="update_name"),
    path('dashboard/update-contact',views.UpdateContact, name="update_contact")
]