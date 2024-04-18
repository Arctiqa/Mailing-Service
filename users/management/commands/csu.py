import os

from django.core.management import BaseCommand
from users.models import User
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='Sinitro@yandex.ru',
            first_name='Roman',
            last_name='Sinitsyn',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('CSU_PASSWORD'))
        user.save()
