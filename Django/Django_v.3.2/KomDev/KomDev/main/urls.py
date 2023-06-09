from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView
from .views import page_not_found

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('404', page_not_found, name='page_404'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
]

handler404 = page_not_found

