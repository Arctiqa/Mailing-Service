from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    telegram = models.CharField(max_length=150, verbose_name='телеграм', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    token = models.CharField(max_length=50, verbose_name='токен')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        permissions = [
            ('set_is_active', 'Может блокировать пользователя')
        ]
