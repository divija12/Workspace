from django.urls import path
from .views import workhome, upload_file,uploaded_files, create_team, team_detail

urlpatterns = [
    path('', workhome, name='workhome'),
    path('upload/', upload_file, name='upload_file'),
    path('uploaded_files/', uploaded_files, name='uploaded_files'),
    path('create/', create_team, name='create'),
    path('my_teams/', team_detail, name='team_list'),
]
