from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import BlogSitemap

sitemaps = {
    'blog': BlogSitemap
}


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('classes', views.classes, name='classes'),
    path('modules/<slug:course_slug>/', views.modules_view, name='modules'),
    #path('404', views.page_not_found, name='page_404'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', views.robots, name='robots'),
]
