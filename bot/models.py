from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Search(models.Model):
    letters = models.CharField(max_length=32)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_search")
