# Generated by Django 4.2.2 on 2023-06-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_product_discountprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='url',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
    ]