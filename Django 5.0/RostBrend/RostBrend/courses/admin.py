from django.contrib import admin
from .models import Course, Module

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

admin.site.site_title = 'Админ-панель MarAnn'
admin.site.site_header = 'Админ-панель MarAnn'


#class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
 #   pass

#admin.site.register(Video, AdminVideo)
