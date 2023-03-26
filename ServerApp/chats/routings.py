from .consumers import PersonalChatConsumer
from django.urls import path

websockets_urlpatterns = [
    path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
]