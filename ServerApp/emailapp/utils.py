import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from django.conf import settings
from .models import Email


def send_email(email):
    """Send an email using SMTP."""
    smtp_server = settings.EMAIL_HOST
    smtp_port = settings.EMAIL_PORT
    smtp_username = settings.EMAIL_HOST_USER
    smtp_password = settings.EMAIL_HOST_PASSWORD

    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = email.recipient
    message['Subject'] = email.subject
    message.attach(MIMEText(email.body))

    # Add attachments to email, if any
    for attachment in email.attachments.all():
        with open(attachment.file.path, 'rb') as f:
            attachment_file = MIMEBase('application', 'octet-stream')
            attachment_file.set_payload(f.read())
            encoders.encode_base64(attachment_file)
            attachment_file.add_header('Content-Disposition', f'attachment; filename={attachment.name}')
            message.attach(attachment_file)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, email.recipient, message.as_string())


def receive_emails():
    """Retrieve unread emails using IMAP."""
    imap_server = settings.EMAIL_IMAP_SERVER
    imap_port = settings.EMAIL_IMAP_PORT
    imap_username = settings.EMAIL_IMAP_USERNAME
    imap_password = settings.EMAIL_IMAP_PASSWORD

    with imaplib.IMAP4_SSL(imap_server, imap_port) as server:
        server.login(imap_username, imap_password)
        server.select()

        # Search for unread messages
        _, messages = server.search(None, 'UNSEEN')

        # Retrieve message IDs and fetch their contents
        for message_id in messages[0].split():
            _, msg = server.fetch(message_id, "(RFC822)")
            message = email.message_from_bytes(msg[0][1])

            # Extract message fields
            sender = message['From']
            recipient = message['To']
            subject = message['Subject']

            # Extract message body
            if message.is_multipart():
                for part in message.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain':
                        body = part.get_payload(decode=True).decode()
            else:
                body = message.get_payload(decode=True).decode()

            # Create Email object and save it to the database
            email = Email.objects.create(sender=sender, recipient=recipient, subject=subject, body=body)
