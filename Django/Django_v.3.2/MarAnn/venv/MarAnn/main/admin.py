from django.contrib import admin
from .models import Blog
from .views import redirect_to_home
from django.utils.safestring import mark_safe


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'get_html_photo', 'date']
    list_display_links = ['title', 'image']
    search_fields = ['title']

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        
    get_html_photo.short_description = "Миниатюра"


admin.site.register(Blog, BlogAdmin)
#admin.site.register(Product, ProductAdmin)
admin.site.login = redirect_to_home

