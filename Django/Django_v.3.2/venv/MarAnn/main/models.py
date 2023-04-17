from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название статьи',max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #views = models.IntegerField('Просмотры', default=1)

    def __str__ (self):
        return f'Задание: {self.title}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
