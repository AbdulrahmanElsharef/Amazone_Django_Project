from django.contrib import admin
from django.urls import path
from . views import ProductList,ProductDetail,add_review,BrandList

app_name='product'

urlpatterns = [
    path('products',ProductList.as_view(),name='Product_List'),
    path('brands',BrandList.as_view(),name='brand_List'),
    path('products/<slug:slug>',ProductDetail.as_view(),name='Product_Detail'),
    path("products/<slug:slug>/add_review", add_review, name="add_review"),
]