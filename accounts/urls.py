from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login',views.Signin, name="login"),
    path('signup',views.Signup, name="signup"),
    path('logout',views.Signout, name="logout")
]