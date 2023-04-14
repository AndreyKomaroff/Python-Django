from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('blog', views.blog),
    path('portfolio', views.portfolio),
]