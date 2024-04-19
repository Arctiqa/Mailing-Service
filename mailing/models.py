from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}

STATUS_CHOICES = [
    ('created', 'Создана'),
    ('active', 'Запущена'),
    ('finished', 'Завершена'),
]
PERIODICITY = [
    ('once', 'один раз'),
    ('daily', 'ежедневно'),
    ('weekly', 'раз в неделю'),
    ('monthly', 'раз в месяц'), ]


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=150, verbose_name='ФИО')
    commentary = models.CharField(max_length=250, verbose_name='комментарий', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'ФИО: {self.name}, email: {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема')
    text = models.TextField(verbose_name='Сообщение')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    start_time = models.DateTimeField(verbose_name='Дата начала рассылки')
    end_time = models.DateTimeField(verbose_name='Дата окончания рассылки')

    periodicity = models.CharField(default='once', max_length=10, choices=PERIODICITY, verbose_name='Периодичность')
    status = models.CharField(default='created', max_length=10, choices=STATUS_CHOICES, verbose_name='Статус рассылки')

    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='сообщение')
    clients = models.ManyToManyField('Client', verbose_name='клиенты')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Активная')

    def __str__(self):
        return f'{self.name}, периодичность: {self.periodicity}, статус: {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

        permissions = [
            ('can_view', 'Может смотреть рассылки')
        ]


class MailingAttempt(models.Model):
    last_success = models.DateTimeField(verbose_name='Дата последнего успешно отправленного сообщения')
    status = models.BooleanField(default=False, verbose_name='Статус отправки')
    server_response = models.TextField(verbose_name='Отклик почтового сервера')

    class Meta:
        verbose_name = 'Статус отправки сообщения'
        verbose_name_plural = 'Статус отправки сообщений'



# class Logs(models.Model):
#     mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)
#     last_mailing_time = models.DateTimeField(auto_now=True, verbose_name='Время рассылки', **NULLABLE)
#     status = models.CharField(default=False, max_length=10, choices=LOG_CHOICES, verbose_name='Попытка', **NULLABLE)
#
#     def __str__(self):
#         return f'{self.last_mailing_time} - {self.status}'
#
#     class Meta:
#         verbose_name = 'Лог сообщения'
#         verbose_name_plural = 'Логов сообщений'