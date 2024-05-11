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
    inlines = (GoodsCharacteristicInline,)

    def get_characteristic(self, obj):
        characteristics = obj.characteristics.all()
        if characteristics:
            return ', '.join(
                [characteristic.name for characteristic in characteristics]
            )
        return '-'

    get_characteristic.short_description = 'Характеристики'

    def get_queryset(self, request):
        return Goods.objects.all().prefetch_related('characteristics')


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Characteristic)
