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
    path('blog/<slug:blog_slug>/', views.show_post, name='post'),
    path('offer_doc/', views.offer_doc, name='offer_doc'),
    path('user_consent/', views.user_consent, name='user_consent'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', views.robots, name='robots')
]
