"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from app.views import first, index, articles, archive, users, article_number, article_number_archive, phone, uniq

urlpatterns = [
    path('', index),
    path('test/', first),
    path('articles/', articles, name='mail_article'),
    path('articles/archive/', archive, name='archive'),
    path('users/', users, name='users'),
    path('article/<int:article_id>/', article_number, name='article with number'),
    path('article/<int:article_id>/archive/', article_number_archive, name='archive with num'),
    path('article/<int:article_id>/<slug:slug_text>/', article_number, name='slug_article'),
    path('users/<int:user_num>/', users, name='users with num'),
    re_path(r'(?P<phone>0(?:98|97|66|67|68)\d{7})/', phone, name='for_correct_phones'),
    re_path(r'(?P<unique>\A([a-f0-9]){4}-([a-f0-9]{6}))\b', uniq, name='unique'),
]
