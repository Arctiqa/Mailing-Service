from django import forms

from blog.models import Blog
from mailing.forms import MixinFormStyle


class BlogForm(MixinFormStyle, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body')
