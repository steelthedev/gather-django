from hashlib import blake2b
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Q




class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username}) |
            Q(**{self.model.EMAIL_FIELD: username})
        )


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=200)
    username = models.CharField(max_length=200, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    time_zone = models.CharField(max_length=200, blank=True, null=True)



    USERNAME_FIELD = "username"
    EMAIL_FIELD ="email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

