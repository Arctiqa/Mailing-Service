from django import forms

from mailing.models import Client, Message, Mailing


class MixinFormStyle:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class ClientForm(MixinFormStyle, forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'commentary']


class MessageForm(MixinFormStyle, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)


class MailingForm(MixinFormStyle, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ('owner', 'status',)

        # widgets = {
        #     'start_date': AdminSplitDateTime(attrs={'placeholder': 'DD.MM.YYYY', 'type': 'date'}),
        #     'end_date': AdminSplitDateTime(attrs={'placeholder': 'DD.MM.YYYY', 'type': 'date'}),
        # }
