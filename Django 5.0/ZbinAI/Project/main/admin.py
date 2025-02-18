from django.contrib import admin
from .models import Blog, Product, Structure
from .views import redirect_to_home
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not \
    field.many_to_many and not field.one_to_many]
# записать первую строку с информацией заголовка
    writer.writerow([field.verbose_name for field in fields])
# записать строки данных
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discountPrice']
    list_display_links = ['title', 'price', 'discountPrice']
    search_fields = ['title']

@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
    list_display_links = ['title', 'text']
    search_fields = ['title']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'get_html_photo', 'created', 'publish']
    list_display_links = ['title', 'image', 'publish']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']
    actions = [export_to_csv]



    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        
    get_html_photo.short_description = "Миниатюра"

#admin.site.register(Blog, BlogAdmin)
#admin.site.register(Product, ProductAdmin)
admin.site.login = redirect_to_home

