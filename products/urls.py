from django.urls import path
from .views import index
from django.contrib import admin


urlpatterns = [
    path('', index, name = 'index')
]