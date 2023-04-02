from django import forms
from .models import File, Team
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class FileForm(forms.ModelForm):
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    class Meta:
        model = File
        fields = ['name', 'description', 'file','team']

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'description', 'members')

    members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

