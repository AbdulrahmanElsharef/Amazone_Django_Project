from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order_list'),
    path('orders/checkout', checkout, name='order_checkout'),
    path('orders/add_to_Cart', add_to_Cart, name='add_to_Cart'),
    
    
]
