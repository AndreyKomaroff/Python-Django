from django.contrib import admin
from .models import Blog
from .views import redirect_to_home


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'date']
    list_display_links = ['title', 'image']
    search_fields = ['title']


admin.site.register(Blog, BlogAdmin)
admin.site.login = redirect_to_home