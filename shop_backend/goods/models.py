from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

User = get_user_model()


def title_shorter(self):
    if len(self.name) > settings.SHORT_NAME_LENGTH:
        return self.name[:settings.SHORT_NAME_LENGTH] + '...'
    return self.name


class Category(models.Model):
    name = models.CharField('Название', max_length=128)
    slug = models.SlugField('Слаг', unique=True, blank=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return title_shorter(self)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Characteristic(models.Model):
    name = models.CharField('Название', max_length=64, unique=True)

    class Meta:
        verbose_name = 'характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return title_shorter(self)


class Characteristic_value(models.Model):
    name = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    value = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'характеристика-значение'
        verbose_name_plural = 'Характеристики-значение'

    def __str__(self):
        return f'{self.name}-{self.value}'


class Goods(models.Model):
    vendor_code = models.CharField('Артикул', max_length=64, unique=True)
    name = models.CharField('Название', max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='goods',
                                 verbose_name='Категория')
    slug = models.SlugField('Слаг', unique=True, blank=True)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2)
    description = models.TextField('Описание', max_length=2000)
    characteristic = models.ManyToManyField(Characteristic_value,
                                            related_name='goods',
                                            verbose_name='Характеристики')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}-{self.vendor_code}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Goods, self).save(*args, **kwargs)
