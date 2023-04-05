from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order_list'),
]
