from django.contrib import admin
from .models import Blog
from .views import redirect_to_home
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'get_html_photo', 'created', 'publish']
    list_display_links = ['title', 'image', 'publish']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']



    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        
    get_html_photo.short_description = "Миниатюра"


#admin.site.register(Blog, BlogAdmin)
#admin.site.register(Product, ProductAdmin)
#admin.site.login = redirect_to_home

