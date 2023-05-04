from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
#from django.views.generic import ListView

    
class Course(models.Model):
    owner = models.ForeignKey(User,
                        related_name='courses_created',
                        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

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
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField()
    order = OrderField(blank=True, for_fields=['course'])

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
                            limit_choices_to={'model__in':(
                                            'text',
                                            'video',
                                            'image',
                                            'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])
    
    class Meta:
        ordering = ['order']


