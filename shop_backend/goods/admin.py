from django.contrib import admin

from .models import Category, Characteristic, Goods


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
    pass
    list_display = ('vendor_code', 'name', 'category', 'price', 'description', 'get_characteristic')
    search_fields = ('name',)
    list_filter = ('price', 'characteristic')

    def get_characteristic(self, obj):
        return ', '.join([one_characteristic.name for one_characteristic in obj.characteristic.all()])
