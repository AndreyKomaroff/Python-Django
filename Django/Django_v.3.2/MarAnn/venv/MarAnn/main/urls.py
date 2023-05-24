from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView
from .views import page_not_found

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('classes', views.classes, name='classes'),
    path('404', page_not_found, name='page_404'),
]

handler404 = page_not_found

