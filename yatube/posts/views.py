from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Страницы сообществ')

def group_posts_detail(request, num):
    return HttpResponse(f'Страница сообщества {num}')