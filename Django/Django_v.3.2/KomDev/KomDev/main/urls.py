from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView, TemplateView
from .views import page_not_found
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import BlogSitemap

sitemaps = {
    'blog': BlogSitemap,
}


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('404', page_not_found, name='page_404'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', views.robots, name='robots'),
]

handler404 = page_not_found

