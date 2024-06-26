# Generated by Django 5.0.4 on 2024-05-06 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=64, unique=True, verbose_name='Артикул')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Слаг')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='GoodsCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=64, verbose_name='Значение')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_characteristic', to='goods.characteristic')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_characteristic', to='goods.goods')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='characteristic',
            field=models.ManyToManyField(related_name='goods', through='goods.GoodsCharacteristic', to='goods.characteristic', verbose_name='Характеристики'),
        ),
    ]
