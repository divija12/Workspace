from django.shortcuts import render, redirect, get_object_or_404
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
        form = EmailForm(request.POST, request.FILES or None)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = request.user
            email.save()
            return redirect('inbox')
    else:
        form = EmailForm()
    return render(request, 'emailapp/compose_email.html', {'form': form})

@login_required
def email_detail(request, email_id):
    email = get_object_or_404(Email, id=email_id, receiver=request.user)
    email.read = True
    email.save()
    return render(request, 'emailapp/email_detail.html', {'email': email})
