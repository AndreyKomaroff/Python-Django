from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import *
from main.models import Blog

# Create your views here.

def home(request):
    return render(request, 'main/home.html', {'title': 'Главная!', 'h1': 'Комарова супер макретолог: быстро, качественно, дорого!'})

def blog(request):
    posts = Blog.objects.all()
    context = {
        'title': 'Блог',
        'h1': 'Посты',
        'posts': posts
    }
    return render(request, 'main/blog.html', context=context)

@login_required
def classes(request):
    posts = Module.objects.all()
    context = {
        'title': 'Уроки',
        'h1': 'Видеоуроки от Супермаркетолог',
        'posts': posts
    }
    return render(request, 'main/classes.html', context=context)