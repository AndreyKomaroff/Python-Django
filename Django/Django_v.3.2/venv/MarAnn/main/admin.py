from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'date']
    list_display_links = ['title', 'image']
    search_fields = ['title']


admin.site.register(Blog, BlogAdmin)