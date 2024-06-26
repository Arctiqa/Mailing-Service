from django.contrib import admin

from mailing.models import Client, Message, Mailing, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'owner')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'owner')


@admin.register(Mailing)
class MessageAdmin(admin.ModelAdmin):
    exclude = ('',)


@admin.register(MailingLog)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'last_success', 'status',)
