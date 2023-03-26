import os
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chats.consumers import PersonalChatConsumer
from chats.routings import websockets_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ServerApp.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websockets_urlpatterns
        )
    )
})
