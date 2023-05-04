from django.contrib import admin
from .models import Course, Module, Product

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discountPrice']
    list_display_links = ['title', 'price', 'discountPrice']
    search_fields = ['title']


#class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
 #   pass

#admin.site.register(Video, AdminVideo)