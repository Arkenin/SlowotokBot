from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Search(models.Model):
    letters = models.CharField(max_length=32)
    date = models.DateTimeField()
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,
                             blank = True,
                             null = True,
                             related_name="user_search")
    ip = models.CharField(max_length=32, blank = True, null = True,)
    def __str__(self) -> str:
        return f'{self.date.strftime("%Y-%m-%d %H:%M")}: {self.user}, {self.letters}, IP: {self.ip}'