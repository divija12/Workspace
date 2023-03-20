from django import forms
from django.contrib.auth.models import User
from .models import Email

class EmailForm(forms.ModelForm):
    receiver = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=forms.CheckboxSelectMultiple())
    subject = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Email
        fields = ['receiver', 'subject', 'body']

