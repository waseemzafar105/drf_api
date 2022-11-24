from django.contrib import admin

# Register your models here.

from .models import Shop, Supplier, Product, SupplyDetails


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

@admin.register(SupplyDetails)
class SupplyDetailsAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'shop_id','product_id', 'quantity')
