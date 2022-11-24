from django.http import JsonResponse
from django.db.models import Count, Sum
from django.db.models.sql.constants import CURSOR

#third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import ShopSerializer, SupplierSerializer, ProductSerializer, SupplyDetailsSerializer
from .models import Shop, Supplier, Product, SupplyDetails

class ShopView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
class SupplierView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
class ProductView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class SupplyDetailsView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = SupplyDetailsSerializer
    queryset = SupplyDetails.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TopSuppliersView(APIView):
    def get(self, request, *args, **kwargs):
        datee = SupplyDetails.objects.raw('SELECT * FROM drf_assessment_SupplyDetails GROUP BY supplier_id_id ORDER BY COUNT(shop_id_id) DESC limit 3')
        print(datee)
        serializer = SupplyDetailsSerializer(datee, many=True)
        return Response(serializer.data)
    

class ShopSearchView(APIView):
    def get(self, request, *args, **kwargs):
        Shop_name = kwargs['shop_name']
        qs = Shop.objects.get(name= Shop_name)
        serializer = ShopSerializer(qs, many=False)
        return Response(serializer.data)
    
class ShopSearchViewId(APIView):
    def get(self, request, *args, **kwargs):
        Shop_id = kwargs['shop_id']
        qs = Shop.objects.get(id= Shop_id)
        serializer = ShopSerializer(qs, many=False)
        return Response(serializer.data)
    
class ShopSupplySearchView(APIView):
    def get(self, request, *args, **kwargs):
        Shop_id = kwargs['shop_id']
        qs = SupplyDetails.objects.filter(shop_id= Shop_id)
        serializer = SupplyDetailsSerializer(qs, many=True)
        return Response(serializer.data)
    

class ShopSupplySearchViewName(APIView):
    def get(self, request, *args, **kwargs):
        shop_name = kwargs['shop_name']
        shop_id = Shop.objects.get(name= shop_name)
        qs = SupplyDetails.objects.filter(shop_id = shop_id)
        serializer = SupplyDetailsSerializer(qs, many=True)
        return Response(serializer.data)
    