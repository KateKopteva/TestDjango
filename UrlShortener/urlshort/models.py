from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    long_url = models.CharField(max_length=2100)
    token = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
