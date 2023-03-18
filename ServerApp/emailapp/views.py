from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Email
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import EmailForm

@login_required
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = request.user
            email.save()
            form.save_m2m()
            messages.success(request, 'Email sent successfully')
            return redirect('inbox')
    else:
        form = EmailForm()
    return render(request, 'mail/send_email.html', {'form': form})

@login_required
def inbox(request):
    emails = Email.objects.filter(receiver=request.user)
    return render(request, 'mail/inbox.html', {'emails': emails})

@login_required
def view_email(request):
    user=request.user
    email = get_object_or_404(Email, receiver=user)
    if request.user != email.sender and request.user != email.receiver:
        return redirect('inbox')
    return render(request, 'mail/view_email.html', {'email': email})

