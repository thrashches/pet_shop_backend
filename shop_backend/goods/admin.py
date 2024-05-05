from django.contrib import admin

from .models import Category, Goods, Characteristic_value


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('vendor_code',
                    'name',
                    'category',
                    'price',
                    'description',
                    'get_characteristic',
                    )
    search_fields = ('name',)
    list_filter = ('price',)

    def get_characteristic(self, obj):
        print(obj.characteristic.name)
        return ', '.join(
            [f'{characteristic.name}-{characteristic.value}' for
             characteristic in obj.characteristic.all()])

    def get_queryset(self, request):
        return Goods.objects.all().prefetch_related('characteristic')

    get_characteristic.short_description = 'Характеристики'


admin.site.register(Category)
admin.site.register(Characteristic_value)
