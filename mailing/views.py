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

    success_url = reverse_lazy('mailing:clients_list')

    def form_valid(self, form):
        new_client = form.save()
        new_client.owner = self.request.user
        new_client.save()
        return super().form_valid(form)


class ClientListView(ListView):
    model = Client

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.has_perm('mailing.can_view'):
            return queryset
        return queryset.filter(owner=self.request.user)


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

    def form_valid(self, form):
        new_message = form.save()
        new_message.owner = self.request.user
        new_message.save()
        return super().form_valid(form)


class MessageListView(ListView):
    model = Message

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.has_perm('mailing.can_view'):
            return queryset
        return queryset.filter(owner=self.request.user)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse('mailing:messages_list')


class MessageDeleteView(DeleteView):
    model = Message

    def get_success_url(self):
        return reverse('mailing:messages_list')
