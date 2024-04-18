from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from mailing.forms import ClientForm, MessageForm, MixinFormControl
from mailing.models import Client, Message


class MailingListView(TemplateView):
    template_name = 'mailing/index.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm

    success_url = reverse_lazy('mailing:index')


class ClientListView(ListView):
    model = Client


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm

    success_url = reverse_lazy('mailing:messages_list')


class MessageListView(ListView):
    model = Message
