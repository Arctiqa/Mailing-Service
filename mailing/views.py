import random

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Blog
from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Message, Mailing, MailingLog
from mailing.services import get_cache_for_mailings, get_cache_for_active_mailings


class IndexListView(TemplateView):
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailings_count'] = get_cache_for_mailings()
        context_data['active_mailings_count'] = get_cache_for_active_mailings()
        blog_list = list(Blog.objects.all())
        random.shuffle(blog_list)
        context_data['blog_list'] = blog_list[:3]
        context_data['clients_count'] = len(Client.objects.all())
        return context_data


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm

    success_url = reverse_lazy('mailing:clients_list')

    def form_valid(self, form):
        new_client = form.save()
        new_client.owner = self.request.user
        new_client.save()
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.has_perm('mailing.can_view'):
            return queryset
        return queryset.filter(owner=self.request.user)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailing:clients_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client

    def get_success_url(self):
        return reverse('mailing:clients_list')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm

    success_url = reverse_lazy('mailing:messages_list')

    def form_valid(self, form):
        new_message = form.save()
        new_message.owner = self.request.user
        new_message.save()
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.has_perm('mailing.can_view'):
            return queryset
        return queryset.filter(owner=self.request.user)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse('mailing:messages_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message

    def get_success_url(self):
        return reverse('mailing:messages_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.has_perm('mailing.can_view'):
            return queryset
        return queryset.filter(owner=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm

    def form_valid(self, form, *args, **kwargs):
        new_mailing = form.save(commit=False)
        new_mailing.owner = self.request.user
        new_mailing.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailing:mailing_list')


class MailingDetailView(LoginRequiredMixin, DetailView):
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


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:mailing_list')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing

    def get_success_url(self):
        return reverse('mailing:mailing_list')


class MailingLogsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = MailingLog
    permission_required = 'mailing.view_mailinglog'
    template_name = 'mailing/logs_list.html'
