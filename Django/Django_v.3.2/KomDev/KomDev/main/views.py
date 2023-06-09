from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from main.models import Blog
from django.http import HttpResponseRedirect
import os

# Create your views here.

menu = [{'title': 'Главная', 'url_name': 'home'},
    {'title': 'Блог', 'url_name': 'blog'}
    ]


def home(request):
    context = {
        'title': 'Главная',
        'menu': menu,
    }

    return render(request, 'main/home.html', context=context)

#@cache_page(60)
def blog(request):
    posts = Blog.objects.all()
    context = {
        'title': 'Блог',
        'h1': 'Блог',
        'posts': posts,
        'menu': menu
    }
    return render(request, 'main/blog.html', context=context)


def redirect_to_home(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        return None

def page_not_found(request, exception):
    return render(request, 'main/404.html', {'title': 'Страница не найдена'})

@cache_page(60)
def show_post(request, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }

    return render(request, 'main/post.html', context=context)


handler404 = page_not_found