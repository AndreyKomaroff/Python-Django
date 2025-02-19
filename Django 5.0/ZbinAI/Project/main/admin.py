from django.contrib import admin
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.utils import timezone
import csv
import datetime

from .models import Blog, Product, Structure


### 🔹 Функция экспорта в CSV
@staticmethod
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta  # Получаем метаданные модели
    response = HttpResponse(content_type='text/csv')  # Устанавливаем заголовки
    response['Content-Disposition'] = f'attachment; filename={opts.verbose_name}.csv'

    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    # Записываем заголовки
    writer.writerow([field.verbose_name for field in fields])

    # Записываем данные объектов
    for obj in queryset:
        writer.writerow([
            getattr(obj, field.name).strftime('%d/%m/%Y') if isinstance(getattr(obj, field.name), datetime.datetime)
            else getattr(obj, field.name) for field in fields
        ])

    return response

export_to_csv.short_description = 'Экспорт в CSV'  # Описание действия в Django Admin



### 🔹 Регистрация модели Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'url')  # Отображаемые поля
    list_display_links = ('title', 'price', 'discount_price', 'url')  # Поля с ссылками на редактирование
    search_fields = ('title',)  # Поиск по заголовку
    actions = [export_to_csv]  # Добавление кнопки экспорта в CSV



### 🔹 Регистрация модели Structure
@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')  # Отображаемые поля
    list_display_links = ('title', 'text')  # Поля с ссылками на редактирование
    search_fields = ('title',)  # Поиск по заголовку
    actions = [export_to_csv]  # Добавление кнопки экспорта в CSV



### 🔹 Регистрация модели Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'get_html_photo', 'created', 'publish')  # Поля в списке
    list_display_links = ('title', 'image', 'publish')  # Поля-ссылки
    search_fields = ('title',)  # Поиск по заголовку
    prepopulated_fields = {'slug': ('title',)}  # Автоматическое заполнение slug
    date_hierarchy = 'publish'  # Упорядочивание по дате
    ordering = ('-publish',)  # Сортировка от новых к старым
    actions = [export_to_csv]  # Добавление кнопки экспорта в CSV

    ### 🔹 Метод для отображения миниатюры изображения
    def get_html_photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")
        return "Нет изображения"

    get_html_photo.short_description = "Миниатюра"  # Название колонки в админке