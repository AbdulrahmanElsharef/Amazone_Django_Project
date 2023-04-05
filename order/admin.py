from django.contrib import admin
from .models import *
# Register your models here.
class OrderDetailInline(admin.TabularInline):
    model=OrderDetail
class CartDetailInline(admin.TabularInline):
    model=CartDetail

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    
class CartAdmin(admin.ModelAdmin):
    inlines = [CartDetailInline]    
    
admin.site.register(Cart,CartAdmin)
admin.site.register(CartDetail)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail,)
