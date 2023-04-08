from rest_framework import serializers
from .models import Product , Brand , ProductReview,ProductImage



class ProductReviewSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model = ProductReview
        fields=['user','rate','review','date']
        # exclude=['id','product']
        
class ProductImageSerializer(serializers.ModelSerializer):
    # user=serializers.StringRelatedField()
    class Meta:
        model = ProductImage
        fields=['image',]
class ProductListSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    # brand=BrandSerializer()
    brand=serializers.StringRelatedField()
    review=ProductReviewSerializer(source='product_reviews',many=True)
    image=ProductImageSerializer(source='product_images',many=True)
    class Meta:
        model = Product
        fields = '__all__'


class BrandListSerializer(serializers.ModelSerializer):
    # product=ProductListSerializer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields=['name','image','slug']
class BrandDetailSerializer(serializers.ModelSerializer):
    product=ProductListSerializer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'