from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField


### 🔹 Модель Курса
class Course(models.Model):
    owner = models.ForeignKey(User,
                              related_name='courses_created',
                              on_delete=models.CASCADE,
                              verbose_name="Создатель")
    title = models.CharField('Название курса', max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField('Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['-created']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Возвращает URL для просмотра курса."""
        return reverse('modules', kwargs={'course_slug': self.slug})

    def get_first_module(self):
        """Возвращает первый модуль курса, если он есть."""
        return self.modules.order_by('order').first()


### 🔹 Модель Модуля (Часть Курса)
class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField('Название модуля', max_length=200)
    image = models.ImageField(upload_to="courses/images/",
                              default='default.jpg',
                              verbose_name="Изображение")
    description = models.TextField('Описание', blank=True)
    url = models.URLField('Ссылка', blank=True, null=True)
    order = OrderField(blank=True, for_fields=['course'], verbose_name="Порядок")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['order']
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return f'{self.order}. {self.title}'

    def get_absolute_url(self):
        """Возвращает URL для просмотра модуля."""
        return reverse('module_detail', kwargs={'pk': self.pk})

    def has_image(self):
        """Проверяет, есть ли у модуля изображение (не дефолтное)."""
        return self.image and self.image.url != 'default.jpg'


### 🔹 Контент (Видео, Текст, Файл, Изображение)
class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('text', 'video', 'image', 'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']
        verbose_name = 'Контент'
        verbose_name_plural = 'Контенты'

    def __str__(self):
        return f'Контент {self.id} ({self.get_content_type()}) для {self.module.title}'

    def get_content_type(self):
        """Возвращает тип контента (текст, видео, изображение или файл)."""
        return self.content_type.model
