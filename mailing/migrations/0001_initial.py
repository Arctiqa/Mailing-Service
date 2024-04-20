# Generated by Django 4.2.2 on 2024-04-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('name', models.TextField(max_length=150, verbose_name='ФИО')),
                ('commentary', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='MailConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Дата начала')),
                ('end_time', models.DateTimeField(verbose_name='Дата окончания')),
            ],
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_success', models.DateTimeField(verbose_name='Дата последнего успешно отправленного сообщения')),
                ('status', models.BooleanField(default=False, verbose_name='Статус отправки')),
                ('server_response', models.TextField(verbose_name='Отклик почтового сервера')),
            ],
            options={
                'verbose_name': 'Статус отправки сообщения',
                'verbose_name_plural': 'Статус отправки сообщений',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Тема')),
                ('text', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
