# Generated by Django 4.2.2 on 2024-04-20 05:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0008_rename_mailingattempt_mailinglog'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='next_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='следующая рассылка'),
        ),
    ]