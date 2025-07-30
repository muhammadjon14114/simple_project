# simple/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Qo‘shimcha maydonlar istasangiz shu yerga yozasiz
    # masalan: phone = models.CharField(max_length=20, blank=True)
    user_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.username
