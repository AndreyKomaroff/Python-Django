from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('classes', views.classes, name='classes'),
    #path('user', authViews.LoginView.as_view(template_name='main/user.html'), name='user'), 
    #path('exit', authViews.LogoutView.as_view(template_name='main/exit.html'), name='exit'), 
]
