from django.urls import path
from .views import inbox, compose_email

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('compose/', compose_email, name='send_email'),
]

