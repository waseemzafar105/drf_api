from rest_framework import serializers
from .models import Shop,Supplier,Product,SupplyDetails

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'name', 'address'
        )

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'name', 'address'
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name','id'
        )

class SupplyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyDetails
        fields = (
            'supplier_id','shop_id','product_id', 'quantity'
        )
