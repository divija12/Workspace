from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    recipient = models.ManyToManyField(User, related_name='received_emails')
    subject = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(null=True, blank=True, upload_to='attachments/')
    read = models.BooleanField(default=False)

