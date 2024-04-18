from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

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


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailing:clients_list')


class ClientDeleteView(DeleteView):
    model = Client

    def get_success_url(self):
        return reverse('mailing:clients_list')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm

    success_url = reverse_lazy('mailing:messages_list')


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse('mailing:messages_list')


class MessageDeleteView(DeleteView):
    model = Message

    def get_success_url(self):
        return reverse('mailing:messages_list')
