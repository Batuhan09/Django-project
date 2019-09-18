from .models import Remark, Contact
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Remark
        fields = ('author', 'text',)
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')