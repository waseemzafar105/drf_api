from django.contrib import admin
from django.urls import path,include

from drf_assessment.views import ShopView, SupplierView, ProductView, SupplyDetailsView, TopSuppliersView, ShopSearchView, ShopSearchViewId, ShopSupplySearchView, ShopSupplySearchViewName

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('shop/', ShopView.as_view(), name='shop'),
    path('supplier/', SupplierView.as_view(), name='supplier'),
    path('product/', ProductView.as_view(), name='product'),
    path('supplydetails/', SupplyDetailsView.as_view(), name='supplydetails'),
    path('topsuppliersview/', TopSuppliersView.as_view(), name='topsuppliersview'),
    path('shopsearchviewid/<shop_id>/', ShopSearchViewId.as_view(), name='shopsearchviewid'),
    path('shopsearchview/<shop_name>/', ShopSearchView.as_view(), name='shopsearchview'),
    path('shopsupplysearchview/<shop_id>/', ShopSupplySearchView.as_view(), name='shopsupplysearchview'),
    path('shopsupplysearchviewname/<shop_name>/', ShopSupplySearchViewName.as_view(), name='shopsupplysearchviewname'),
]
