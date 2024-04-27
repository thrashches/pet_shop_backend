from django.db import models
from django.template.defaultfilters import slugify

SHORT_NAME_LENGTH = 10


class Category(models.Model):
    name = models.CharField('Название', max_length=128)
    slug = models.SlugField('Слаг', unique=True, blank=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

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
        return self.name[:SHORT_NAME_LENGTH]


class Goods(models.Model):
    vendor_code = models.CharField('Артикул', max_length=64, unique=True)
    name = models.CharField('Название', max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods', verbose_name='Категория')
    slug = models.SlugField('Слаг', unique=True, blank=True)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2)
    description = models.TextField('Описание', max_length=2000)
    characteristic = models.ManyToManyField(Characteristic, related_name='goods', verbose_name='Характеристики')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:SHORT_NAME_LENGTH]

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Goods, self).save(*args, **kwargs)


class Warehouse(models.Model):
    product = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} - {self.quantity} things'
