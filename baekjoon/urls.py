from django.contrib import admin
from django.urls import path
from .views import *

app_name='boj'
urlpatterns = [
    path('', index, name='event'),
]
