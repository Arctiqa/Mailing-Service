import smtplib
from datetime import datetime, timedelta
import pytz
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings

from config.settings import CACHE_ENABLED
from mailing.models import Mailing, MailingLog


def my_job():
    day = timedelta(days=0, minutes=4)
    week = timedelta(days=7)
    month = timedelta(days=30)

    mailings = Mailing.objects.all().filter(status__in=['created', 'active']) \
        .filter(is_active=True) \
        .filter(next_time__lte=datetime.now(pytz.timezone('Asia/Irkutsk'))) \
        .filter(end_time__gte=datetime.now(pytz.timezone('Asia/Irkutsk')))

    print(mailings)

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

        log = MailingLog(mailing=mail, status=status, server_response=server_response, last_success=mail.next_time)
        log.save()

        if mail.periodicity == 'once':
            mail.next_time = mail.start_time
        elif mail.periodicity == 'daily':
            mail.next_time = mail.next_time + day
        elif mail.periodicity == 'weekly':
            mail.next_time = mail.next_time + week
        elif mail.periodicity == 'monthly':
            mail.next_time = mail.next_time + month

        if mail.next_time < mail.end_time:
            mail.status = 'active'
        else:
            mail.status = 'finished'
            mail.is_active = False

        print('mail:', mail)
        mail.save()


def get_mailing_logs_from_cache():
    if not CACHE_ENABLED:
        return MailingLog.objects.all()
    key = 'mailings_count'
    mailing_logs = cache.get(key)
    if mailing_logs is not None:
        return mailing_logs

    mailings_count = MailingLog.objects.all()
    cache.set(key, mailings_count)

    return mailings_count

