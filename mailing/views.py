import random

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Blog
from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Message, Mailing, MailingLog


class IndexListView(TemplateView):
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailings_count'] = Mailing.objects.all().count()
        context_data['active_mailings_count'] = Mailing.objects.filter(is_active=True).count()
        blog_list = list(Blog.objects.all())
        random.shuffle(blog_list)
        context_data['blog_list'] = Blog.objects.filter(is_published=True)[:3]
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

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user or self.request.user.has_perm('mailing.change_client'):
            return obj
        return PermissionDenied


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client

    def get_success_url(self):
        return reverse('mailing:clients_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user or self.request.user.has_perm('mailing.delete_client'):
            return obj
        return PermissionDenied


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

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user or self.request.user.has_perm('mailing.change_message'):
            return obj
        return PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message

    def get_success_url(self):
        return reverse('mailing:messages_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user or self.request.user.has_perm('mailing.delete_message'):
            return obj
        return PermissionDenied


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

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user or self.request.user.has_perm('mailing.change_mailing'):
            return obj
        return PermissionDenied


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing

    def get_success_url(self):
        return reverse('mailing:mailing_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user or self.request.user.has_perm('mailing.delete_mailing'):
            return obj
        return PermissionDenied


class MailingLogsListView(LoginRequiredMixin, ListView):
    model = MailingLog
    template_name = 'mailing/logs_list.html'
