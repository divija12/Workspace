from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Email
from .forms import EmailForm

@login_required
def inbox(request):
    received_emails = Email.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'emailapp/inbox.html', {'received_emails': received_emails})

@login_required
def compose_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES or None)
        if form.is_valid():
            email = form.save(commit=False)
            recipients = form.cleaned_data['recipient']
            email.sender = request.user
            email.save()
            email.recipient.add(*recipients)
            return redirect('inbox')
    else:
        form = EmailForm()
    return render(request, 'emailapp/compose_email.html', {'form': form})

@login_required
def email_detail(request, email_id):
    email = get_object_or_404(Email, id=email_id, recipient=request.user)
    email.read = True
    email.save()
    return render(request, 'emailapp/email_detail.html', {'email': email})


@login_required
def delete_email(request, email_id):
    email = get_object_or_404(Email, id=email_id)
    recipient_count = email.recipient.count()
    if recipient_count > 1:
        email.recipient.remove(request.user)
        email.save()
    else:
        email.delete()
    return redirect('inbox')

@login_required
def reply_to_email(request, email_id):
    email = get_object_or_404(Email, id=email_id)
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES or None)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.save()
            reply.recipient.add(email.sender)
            reply.parent = email
            reply.save()
            return redirect('inbox')
    else:
        new_line = '\n'
        initial_data = {
            'recipient': [email.sender.email],
            'subject': f"Re: {email.subject}",
            'body': f"{new_line}{new_line}{new_line}---{new_line}{email.sender} wrote:{new_line}> {email.body}"
        }
        form = EmailForm(initial=initial_data)
    return render(request, 'emailapp/compose_email.html', {'form': form})

@login_required
def mark_as_read_unread(request, email_id):
    email = get_object_or_404(Email, id=email_id, recipient=request.user)
    if email.read:
        email.read = False
    else:
        email.read = True
    email.save()
    return redirect('inbox')
