# Generated by Django 4.2.1 on 2023-05-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Основной текст статьи')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('discountPrice', models.IntegerField(verbose_name='Стоимость со скидкой')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Предложения',
            },
        ),
    ]