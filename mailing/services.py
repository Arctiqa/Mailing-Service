import smtplib
from datetime import datetime, timedelta
import pytz
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from mailing.models import Mailing, MailingLog


def my_job():
    day = timedelta(days=1, hours=0, minutes=0)
    week = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)

    mailings = Mailing.objects.all().filter(status='created') \
        .filter(is_active=True) \
        .filter(next_time__lte=datetime.now(pytz.timezone('Asia/Irkutsk'))) \
        .filter(end_time__gte=datetime.now(pytz.timezone('Asia/Irkutsk')))

    for mail in mailings:
        mail.status = 'active'
        mail.save()
        emails_list = [client.email for client in mail.clients.all()]

        try:
            send_mail(
                subject=mail.message.title,
                message=mail.message.text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=emails_list,
                fail_silently=False,
            )
            status = 'message sent'
            server_response = 'success'
        except smtplib.SMTPException as e:
            status = 'error'
            server_response = str(e)

        log = MailingLog(mailing=mail, status=status, server_response=server_response, last_success=timezone.now())
        log.save()

        if mail.periodicity == 'once':
            mail.next_time = mail.end_time
        elif mail.periodicity == 'daily':
            mail.next_time = log.last_success + day
        elif mail.periodicity == 'weekly':
            mail.next_time = log.last_success + week
        elif mail.periodicity == 'monthly':
            mail.next_time = log.last_success + month

        if mail.next_time < mail.end_time:
            mail.status = 'active'
        else:
            mail.status = 'finished'
            mail.is_active = False
        mail.save()


def get_cache_for_mailings():
    if settings.CACHE_ENABLED:
        key = 'mailings_count'
        mailings_count = cache.get(key)
        if mailings_count is None:
            mailings_count = Mailing.objects.all().count()
            cache.set(key, mailings_count)
    else:
        mailings_count = Mailing.objects.all().count()
    return mailings_count


def get_cache_for_active_mailings():
    if settings.CACHE_ENABLED:
        key = 'active_mailings_count'
        active_mailings_count = cache.get(key)
        if active_mailings_count is None:
            active_mailings_count = Mailing.objects.filter(is_active=True).count()
            cache.set(key, active_mailings_count)
    else:
        active_mailings_count = Mailing.objects.filter(is_active=True).count()
    return active_mailings_count
