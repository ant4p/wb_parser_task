# Generated by Django 5.2.3 on 2025-06-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость товара')),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость товара со скидкой')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Рейтинг')),
                ('reviews', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'products',
            },
        ),
    ]
