# Generated by Django 5.2.3 on 2025-07-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(verbose_name='Рейтинг'),
        ),
    ]
