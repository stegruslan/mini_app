from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    email = models.EmailField(unique=True)


class Profile(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"
