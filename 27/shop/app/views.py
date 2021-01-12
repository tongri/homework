from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def first(request):
    return HttpResponse("Hello")

def index(request):
    return HttpResponse("index")

def articles(request):
    return HttpResponse('There will be a list with articles')


def archive(request):
    return HttpResponse('This is page for archived articles')

def users(request, user_num=0):
    return HttpResponse(f'page for user {user_num}' if user_num else f'page for users')

def article_number(request, article_id, slug_text=''):
    return HttpResponse(f'the number of article is {article_id} with text {slug_text}' if slug_text else
                        f'the number of article is {article_id}')

def article_number_archive(request, article_id):
    return HttpResponse(f'the number of archive article is {article_id}')

def phone(request, phone=''):
    return HttpResponse(f'your phone number is correct - it is {phone}')

def uniq(request, unique):
    return HttpResponse(f'glad 2 see u {unique}')
