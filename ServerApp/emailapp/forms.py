from django import forms
from django.contrib.auth.models import User
from .models import Email

class EmailForm(forms.ModelForm):
    recipient = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)
    subject = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(required=False)

    class Meta:
        model = Email
        fields = ['recipient', 'subject', 'body', 'file']

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].widget.attrs['class'] = 'form-control select2'
        self.fields['recipient'].widget.attrs['multiple'] = 'multiple'
        self.fields['recipient'].widget.attrs['data-placeholder'] = 'Select recipient'
