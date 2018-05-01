from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    nickname = models.CharField('昵称',max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass