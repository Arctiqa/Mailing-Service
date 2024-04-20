from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Message, Mailing, MailingLog


class IndexListView(TemplateView):
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


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.has_perm('mailing.can_view'):
            return queryset
        return queryset.filter(owner=self.request.user)


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm

    def form_valid(self, form, *args, **kwargs):
        new_mailing = form.save(commit=False)
        new_mailing.owner = self.request.user
        new_mailing.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailing:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        clients = self.object.clients.all()
        formatted_clients = []

        for client in clients:
            formatted_client = {'client_name': client.name, 'client_email': client.email}
            formatted_clients.append(formatted_client)

        context_data['clients'] = formatted_clients
        return context_data


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing

    def get_success_url(self):
        return reverse('mailing:mailing_list')


class MailingLogsListView(ListView):
    model = MailingLog
    template_name = 'mailing/logs_list.html'

