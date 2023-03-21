from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Email
from .forms import EmailForm

@login_required
def inbox(request):
    received_emails = Email.objects.filter(receiver=request.user).order_by('-sent_at')
    return render(request, 'emailapp/inbox.html', {'received_emails': received_emails})

@login_required
def compose_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = request.user
            email.save()
            return redirect('inbox')
    else:
        form = EmailForm()
    return render(request, 'emailapp/compose_email.html', {'form': form})

