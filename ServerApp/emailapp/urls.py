from django.urls import path
from .views import inbox, compose_email, email_detail

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('compose/', compose_email, name='send_email'),
    path('email/<int:email_id>/', email_detail, name='email_detail'),
]

