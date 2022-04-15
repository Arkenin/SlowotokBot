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
    def __str__(self) -> str:
        return f'{self.user}: {self.letters}'