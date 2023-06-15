from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from courses.models import Module, Product, Course
from main.models import Blog
from django.http import HttpResponse, HttpResponseRedirect
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

@cache_page(60)
def blog(request):
    posts = Blog.objects.all()
    context = {
        'title': 'Блог',
        'h1': 'Блог',
        'posts': posts,
        'menu': menu
    }

    return render(request, 'main/blog.html', context=context)

#@cache_page(60)
@login_required
def classes(request):
    courses = Course.objects.all()
    #posts = Module.objects.all()

    course_slug = request.GET.get('course', None)
    if course_slug:
        course = Course.objects.get(slug=course_slug)
        modules = Module.objects.filter(course=course)
    else:
        course = None
        modules = None

    context = {
        'title': 'Уроки',
        'h1': 'Видеоуроки от Супермаркетолог',
        'menu': menu,
        'courses': courses,
        'selected_course': course,
        'modules': modules    
    }
    
    return render(request, 'main/classes.html', context=context)

def modules_view(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    modules = course.modules.all()
    return render(request, 'main/modules.html', {'menu': menu, 'course': course, 'modules': modules})

def redirect_to_home(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        return None

def page_not_found(request, exception):
    return render(request, 'main/404.html', status=404)

#@cache_page(60)
def show_post(request, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }

    return render(request, 'main/post.html', context=context)

def robots(request):
    content = "User-agent: *\nDisallow: /admin/\nDisallow: /classes/\nDisallow: /database/"
    response = HttpResponse(content, content_type='text/plain')
    return response

handler404 = page_not_found