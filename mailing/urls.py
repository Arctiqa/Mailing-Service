from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import IndexListView, ClientCreateView, MessageCreateView, MessageListView, ClientListView, \
    ClientUpdateView, MessageUpdateView, MessageDeleteView, ClientDeleteView, MailingListView, MailingCreateView, \
    MailingDetailView, MailingUpdateView, MailingDeleteView, MailingLogsListView

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('client/list', ClientListView.as_view(), name='clients_list'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('client/edit/<int:pk>', ClientUpdateView.as_view(), name='client_edit'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('messages_list', MessageListView.as_view(), name='messages_list'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('messages/edit/<int:pk>', MessageUpdateView.as_view(), name='messages_edit'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='messages_delete'),

    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/view/<int:pk>', MailingDetailView.as_view(), name='mailing_view'),
    path('mailing/edit/<int:pk>', MailingUpdateView.as_view(), name='mailing_edit'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('log_list/', MailingLogsListView.as_view(), name='log_list'),

]
