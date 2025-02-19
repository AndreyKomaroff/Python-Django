from django.db import models
from django.utils import timezone
from django.urls import reverse

# Базовая модель с общими полями (абстрактный класс)
class AbstractBaseModel(models.Model):
    title = models.CharField('Название', max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    class Meta:
        abstract = True  # Указывает, что это базовый класс (не создаст таблицу)

    def __str__(self):
        return self.title

# Модель товара
class Product(AbstractBaseModel):
    text = models.TextField('Описание')
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2, default=0.00)
    discount_price = models.DecimalField('Стоимость со скидкой', max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)
    url = models.URLField('Ссылка')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

# Модель структуры
class Structure(AbstractBaseModel):
    text = models.TextField('Описание')

    class Meta:
        verbose_name = 'Структура'
        verbose_name_plural = 'Структуры'

    def get_absolute_url(self):
        return reverse('structure_detail', kwargs={'pk': self.pk})

# Модель блога
class Blog(AbstractBaseModel):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    image = models.ImageField(upload_to="media/blog", verbose_name="Изображение")
    text = models.TextField('Основной текст')
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def get_absolute_url(self):
        return reverse('post', kwargs={'blog_slug': self.slug})
