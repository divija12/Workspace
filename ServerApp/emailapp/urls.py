from django.urls import path
from .views import *

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('compose/', compose_email, name='send_email'),
    path('email/<int:email_id>/', email_detail, name='email_detail'),
    path('<int:email_id>/reply/', reply_to_email, name='reply_email'),
    path('delete/<int:email_id>/', delete_email, name='delete_email'),
    path('read_unread/<int:email_id>/', mark_as_read_unread, name='mark_as_read_unread'),
]

