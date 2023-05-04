from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve as mediaserve
#from django.conf.urls import url

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(),
        name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
        name='logout'),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = pageNotFound    