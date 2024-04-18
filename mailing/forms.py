from django import forms

from mailing.models import Client, Message


class MixinFormControl:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(MixinFormControl, forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'commentary']


class MessageForm(MixinFormControl, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
