from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from blog.models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
    {'title': 'Блог', 'url_name': 'blog'}]

def home(request):
    context = {
        'title': 'Главная',
        'menu': menu,
    }

    return render(request, 'blog/home.html', context=context)

def blog(request):
    posts = Post.objects.all()
    context = {
        'title': 'Блог',
        'h1': 'Посты',
        'posts': posts,
        'menu': menu
    }
    return render(request, 'blog/blog.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }

    return render(request, 'blog/post.html', context=context)

