from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('todo/', views.todoappView, name='todo'),
    path('update_task/<str:new_name>/', views.updateTask, name='update_task'),
    path('delete_task/<int:id>/', views.deleteTask, name='delete_task'),
]
