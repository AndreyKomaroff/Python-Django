from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from courses.models import *
from main.models import Blog
from django.http import HttpResponseRedirect
import os

# Create your views here.

menu = [{'title': 'Главная', 'url_name': 'home'},
    {'title': 'Блог', 'url_name': 'blog'},
    {'title': 'Уроки', 'url_name': 'classes'}]


def home(request):
    items = Product.objects.all()
    context = {
        'title': 'Главная',
        'menu': menu,
        'items': items
    }

    return render(request, 'main/home.html', context=context)

def blog(request):
    posts = Blog.objects.all()
    context = {
        'title': 'Блог',
        'h1': 'Посты',
        'posts': posts,
        'menu': menu
    }
    return render(request, 'main/blog.html', context=context)

@login_required
def classes(request):
    posts = Module.objects.all()
    context = {
        'title': 'Уроки',
        'h1': 'Видеоуроки от Супермаркетолог',
        'posts': posts,
        'menu': menu
    }
    return render(request, 'main/classes.html', context=context)

def redirect_to_home(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        return None
