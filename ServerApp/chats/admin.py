from django.contrib import admin
from chats.models import ChatModel, UserProfileModel, ChatNotification
admin.site.register(ChatModel)
admin.site.register(UserProfileModel)
admin.site.register(ChatNotification)