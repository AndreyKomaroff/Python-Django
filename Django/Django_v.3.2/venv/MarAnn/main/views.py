from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import *

# Create your views here.

def home(request):
    return render(request, 'main/home.html', {'title': 'Главная!', 'h1': 'Комарова супер макретолог: быстро, качественно, дорого!'})

def blog(request):
    return render(request, 'main/blog.html', {'title': 'Блог', 'h1': 'Блог'})

def portfolio(request):
    return render(request, 'main/portfolio.html', {'title': 'Портфолио', 'h1': 'Портфолио'})

@login_required
def classes(request):
    posts = Module.objects.all()
    context = {
        'title': 'Уроки',
        'h1': 'Видеоуроки от Супермаркетолог',
        'posts': posts
    }
    return render(request, 'main/classes.html', context=context)