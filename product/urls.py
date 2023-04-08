from django.contrib import admin
from django.urls import path
from . views import ProductList,ProductDetail,add_review,BrandList,BrandDetail
from .api import ProductListApi,ProductDetailUpdateApi,BrandListApi,BrandDetailUpdateApi
app_name='product'

urlpatterns = [
    #api

    path('api/list',ProductListApi.as_view(),name='product_list_api'),
    path('api/list/brands',BrandListApi.as_view(),name='brand_list_api'),
    path('api/list/<slug:slug>',ProductDetailUpdateApi.as_view(),name='product_detail_Update_api'),
    path('api/list/brands/<slug:slug>',BrandDetailUpdateApi.as_view(),name='brand_detail_Update_api'),
    #apps
    path('products',ProductList.as_view(),name='Product_List'),
    path('products/<slug:slug>',ProductDetail.as_view(),name='Product_Detail'),
    path("products/<slug:slug>/add_review", add_review, name="add_review"),
    path('brands',BrandList.as_view(),name='brand_List'),
    path('brands/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),
]