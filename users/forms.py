from django import forms

from mailing.forms import MixinFormStyle
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm

from users.models import User


class UserRegisterForm(MixinFormStyle, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(MixinFormStyle, UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'telegram')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class ResetPasswordForm(MixinFormStyle, PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
        except Exception:
            raise forms.ValidationError('Пользователь с такой почтой не зарегистрирован')

        return email

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email,
                  html_email_template_name=None):
        pass
