from django.contrib import admin
from django.urls import path,include
from .views import home,employdata,logoutUser
from chats.views import index, chatPage

urlpatterns = [
    path('', home, name='home'),

    path('home/', employdata, name='employdata'),
  
    path('logout/', logoutUser, name='logout'),
 
    path('workspace/', include('workspace.urls')),

    path('email/', include('emailapp.urls')),

    path('calendar/', include('calendarapp.urls')),

    path('', include('todo.urls')),

    path('chat/<str:username>/', chatPage, name='chat'),

]