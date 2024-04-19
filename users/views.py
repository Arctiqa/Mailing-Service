import secrets
import string

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm, ResetPasswordForm
from users.models import User
from config import settings


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:new_email_verify')

    def form_valid(self, form):
        user = form.save()
        token = secrets.token_hex(16)
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/verify/{token}'
        message = f'Для подтверждения верификации почты необходимо перейти по ссылке: {url}'
        send_mail('Верификация почты', message, settings.EMAIL_HOST_USER, [user.email])
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('mailing:index')

    def get_object(self, queryset=None):
        return self.request.user


def verify(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ResetPasswordView(PasswordResetView):

    form_class = ResetPasswordForm
    template_name = 'users/reset_password.html'
    email_template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('users:new_pass_generate')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)

        alphabet = string.ascii_letters + string.digits
        password = "".join(secrets.choice(alphabet) for i in range(10))
        user.password = make_password(password)
        user.save()
        message = f"Ваш новый пароль:\n{password}"
        send_mail(
            "Смена пароля",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class NewPassGenerateView(TemplateView):
    template_name = 'users/new_pass_generate.html'


class NewEmailVerify(TemplateView):
    template_name = 'users/new_email_verify.html'
