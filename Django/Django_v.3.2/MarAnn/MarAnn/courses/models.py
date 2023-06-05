from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
#from django.views.generic import ListView

    
class Course(models.Model):
    owner = models.ForeignKey(User,
                        related_name='courses_created',
                        on_delete=models.CASCADE, verbose_name="Создатель")
    title = models.CharField('Название курса', max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField('Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        ordering = ['-created']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


    def __str__(self):
        return self.title
    
class Module(models.Model):
    course = models.ForeignKey(Course,
                        related_name='modules',
                        on_delete=models.CASCADE)
    title = models.CharField('Название модуля', max_length=200)
    image = models.ImageField(upload_to="media/courses", default='image', verbose_name="Изображение")
    description = models.TextField('Описание', blank=True)
    url = models.URLField('Ссылка')
    order = OrderField(blank=True, for_fields=['course'], verbose_name="Номер п/п")

    class Meta:
        ordering = ['order']
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return f'{self.order}. {self.title}'
    
class Content(models.Model):
    module = models.ForeignKey(Module,
                            related_name='contents',
                            on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                            on_delete=models.CASCADE,
                            limit_choices_to={'model__in':('text', 'video', 'image', 'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])
    
    class Meta:
        ordering = ['order']

class Product(models.Model):
    title = models.CharField('Название',max_length=100, unique=True)
    #image = models.ImageField(upload_to="media/blog", verbose_name="Фото")
    text = models.TextField('Основной текст статьи')
    price = models.IntegerField('Стоимость')
    discountPrice = models.IntegerField('Стоимость со скидкой')
    url = models.URLField('Ссылка')

    def __str__ (self):
        return f'Предложения: {self.title}'

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

