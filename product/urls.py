from django.contrib import admin
from django.urls import path
from . views import ProductList,ProductDetail

app_name='product'

urlpatterns = [
    path('products',ProductList.as_view(),name='Product_List'),
    path('products/<slug:slug>',ProductDetail.as_view(),name='Product_Detail'),
]