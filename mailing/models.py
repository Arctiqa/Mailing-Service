from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


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


class MailConfig(models.Model):
    start_time = models.DateTimeField(verbose_name='Дата начала')
    end_time = models.DateTimeField(verbose_name='Дата окончания')
    periodicity = [('daily', 'ежедневная'), ('weekly', 'еженедельная'), ('monthly', 'ежемесячная')]

    status = [('completed', ' завершена'), ('created', 'создана'), ('started', 'запущена')]

    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='сообщение')
    client = models.ManyToManyField('Client', verbose_name='клиент')

    def __str__(self):
        return f'{self.start_time} - {self.end_time}, периодичность: {self.periodicity}, статус: {self.status}'


class MailingAttempt(models.Model):
    last_success = models.DateTimeField(verbose_name='Дата последнего успешно отправленного сообщения')
    status = models.BooleanField(default=False, verbose_name='Статус отправки')
    server_response = models.TextField(verbose_name='Отклик почтового сервера')

    class Meta:
        verbose_name = 'Статус отправки сообщения'
        verbose_name_plural = 'Статус отправки сообщений'
