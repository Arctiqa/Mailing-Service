from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, ClientCreateView, MessageCreateView, MessageListView, ClientListView, \
    ClientUpdateView, MessageUpdateView, MessageDeleteView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='index'),
    path('client/list', ClientListView.as_view(), name='clients_list'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('client/edit/<int:pk>', ClientUpdateView.as_view(), name='client_edit'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('messages_list', MessageListView.as_view(), name='messages_list'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('messages/edit/<int:pk>', MessageUpdateView.as_view(), name='messages_edit'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='messages_delete'),

]
