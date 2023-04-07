from django.contrib import admin
from django.urls import path
from . views import ProductList,ProductDetail,add_review,BrandList,BrandDetail
from .api import ProductListApi,ProductDetailUpdateApi,BrandListApi
app_name='product'

urlpatterns = [
    path('products/api/list',ProductListApi.as_view(),name='product_list_api'),
    path('brands/api/list',BrandListApi.as_view(),name='brand_list_api'),
    path('products/api/list/<slug:slug>',ProductDetailUpdateApi.as_view(),name='product_detail_Update_api'),

    
    path('products',ProductList.as_view(),name='Product_List'),
    path('products/<slug:slug>',ProductDetail.as_view(),name='Product_Detail'),
    path("products/<slug:slug>/add_review", add_review, name="add_review"),
    path('brands',BrandList.as_view(),name='brand_List'),
    path('brands/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),

#api
]