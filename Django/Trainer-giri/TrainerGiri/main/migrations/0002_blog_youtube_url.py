# Generated by Django 4.2.2 on 2023-06-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='youtube_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на видео в YouTube'),
        ),
    ]