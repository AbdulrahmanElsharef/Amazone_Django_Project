from django.contrib import admin
from .models import *
# Register your models here.
class ImageInline(admin.TabularInline):
    model=ProductImage
class ReviewInline(admin.TabularInline):
    model=ProductReview

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline,ReviewInline]
    list_display = ['id','name', 'price']
    list_filter=['brand','flag']
    search_fields=['name','subtitle','slug']

admin.site.register(Brand)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)


