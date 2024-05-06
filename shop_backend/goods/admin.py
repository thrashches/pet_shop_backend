from django.contrib import admin

from .models import Category, Goods, GoodsCharacteristic, Characteristic


class GoodsCharacteristicInline(admin.TabularInline):
    model = GoodsCharacteristic


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('vendor_code',
                    'name',
                    'category',
                    'price',
                    'description',
                    'get_characteristic',
                    )

    readonly_fields = ('slug',)
    search_fields = ('name',)
    list_filter = ('price',)

    def get_characteristic(self, obj):
        return ', '.join(
            [f'{characteristic.characteristic}-{characteristic.value}' for
             characteristic in obj.goods_characteristic.all()])

    def get_queryset(self, request):
        return Goods.objects.all().prefetch_related('characteristic')

    inlines = (GoodsCharacteristicInline,)

    get_characteristic.short_description = 'Характеристики'


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Characteristic)
admin.site.register(GoodsCharacteristic)
