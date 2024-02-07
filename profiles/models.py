from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


title = models.CharField(max_length=250)
slug = models.SlugField(max_length=250)
author = models.ForeignKey(User, on_delete=models.CASCADE)
body = models.TextField()
publish = models.DateTimeField(default=timezone.now)
