from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликован'

    title = models.CharField('Название статьи', max_length=250, unique=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name="Изображение")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Автор")
    text = models.TextField('Основной текст статьи')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name="Статус")

    def __str__(self):
        return f'Пост: {self.title}'

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

