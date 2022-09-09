from .views import *
from django.urls import path,include


app_name='mainapp'

urlpatterns=[
    path('', bot , name='bot'),
    path('/botreply', botreply , name='botreply'),
]