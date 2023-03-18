from django.urls import path
from.views import send_email,inbox,view_email

urlpatterns = [
    path('send_email/', send_email, name='send_email'),
        path('inbox/', inbox, name='inbox'),
    path('view_email/', view_email, name='view_email')
]