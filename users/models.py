from django.db import models
from django.contrib.auth.models import AbstractUser


class Roles(models.Model):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    roles = models.ManyToManyField(Roles, related_name="user_roles")
    
    def __str__(self):
        return f"{self.username} : {self.email}"
