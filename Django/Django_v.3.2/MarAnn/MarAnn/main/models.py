from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField('Название статьи', max_length=250, unique=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to="media/blog", verbose_name="Изображение")
    text = models.TextField('Основной текст статьи')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата")

    def __str__ (self):
        return f'Пост: {self.title}'

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', kwargs={'blog_slug': self.slug})


