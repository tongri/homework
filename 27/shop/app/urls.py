from django.contrib import admin
from django.urls import path, include

from app.views import first

urlpatterns = [
    path('test/', first)
]