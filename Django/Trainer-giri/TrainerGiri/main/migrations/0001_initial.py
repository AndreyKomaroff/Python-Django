# Generated by Django 4.2.2 on 2023-06-20 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Название статьи')),
                ('slug', models.SlugField(max_length=255, verbose_name='URL')),
                ('image', models.ImageField(upload_to='media/blog', verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Основной текст статьи')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-publish'],
                'indexes': [models.Index(fields=['-publish'], name='main_blog_publish_52a62a_idx')],
            },
        ),
    ]