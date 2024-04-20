# Generated by Django 4.2.2 on 2024-04-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_remove_mailing_client_mailing_clients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingattempt',
            name='mailing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='рассылка'),
        ),
        migrations.AlterField(
            model_name='mailingattempt',
            name='last_success',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего успешно отправленного сообщения'),
        ),
        migrations.AlterField(
            model_name='mailingattempt',
            name='server_response',
            field=models.TextField(blank=True, null=True, verbose_name='Отклик почтового сервера'),
        ),
        migrations.AlterField(
            model_name='mailingattempt',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Статус отправки'),
        ),
    ]
