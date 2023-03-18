from django.contrib import admin
from django.urls import path,include
from .views import home,employdata,logoutUser

urlpatterns = [
    path('home/', home, name='home'),

    path('employdata/',employdata, name='employdata'),
  
    path('logout/',logoutUser, name='logout'),
 
    path('workspace/',include('workspace.urls')),

    path('email/',include('emailapp.urls'))

]