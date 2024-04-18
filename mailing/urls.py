from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, ClientCreateView, MessageCreateView, MessageListView, ClientListView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='index'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('messages_list', MessageListView.as_view(), name='messages_list'),
    path('client/list', ClientListView.as_view(), name='clients_list')
]
