# Generated by Django 4.2.2 on 2024-04-20 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0009_mailing_next_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailing',
            old_name='next_date',
            new_name='next_time',
        ),
    ]
