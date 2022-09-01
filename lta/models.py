from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, default="avatar.png", upload_to='images/')

    USERNAME_FIELDS = "email"
    REQUIRED_FIELDS = []
