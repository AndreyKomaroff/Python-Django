from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('classes', views.classes, name='classes'),

]
