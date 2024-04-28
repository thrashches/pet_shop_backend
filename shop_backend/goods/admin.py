from django.contrib import admin

from .models import Category, Characteristic, Goods, ProductBasket


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('vendor_code', 'name', 'category', 'price', 'description', 'get_characteristic')
    search_fields = ('name',)
    list_filter = ('price', 'characteristic')

    def get_characteristic(self, obj):
        return ', '.join([one_characteristic.name for one_characteristic in obj.characteristic.all()])
@admin.register(ProductBasket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('customer', 'get_products', 'quantity')
    search_fields = ('customer',)
    list_filter = ('customer', 'products')

    def get_products(self, obj):
        return ', '.join([product.name for product in obj.products.all()])
