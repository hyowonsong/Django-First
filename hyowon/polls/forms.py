from django import forms
from .validators import validate_com

from django.forms import ModelForm
from .models import Contact


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(validators=[validate_com])
    cc_myself = forms.BooleanField(required=False)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'message', 'sender']
        # exclude = ['cc_myself']
        # fields = '__all__'
