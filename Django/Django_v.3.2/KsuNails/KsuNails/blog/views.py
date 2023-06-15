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

def page_not_found(request, exception):
    return render(request, 'blog/404.html', status=404)

def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }

    return render(request, 'blog/post.html', context=context)

def robots(request):
    content = "User-agent: *\nDisallow: /admin/\nDisallow: /database/"
    response = HttpResponse(content, content_type='text/plain')
    return response

handler404 = page_not_found