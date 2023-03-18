from django import forms
from django.contrib.auth.models import User
from .models import Email

class EmailForm(forms.ModelForm):
    recipients = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Email
        fields = ['subject', 'message', 'recipients']
