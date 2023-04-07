from rest_framework import serializers
from .models import Product , Brand , ProductReview



class ProductReviewSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model = ProductReview
        # fields=['user','rate','review','date']
        exclude=['id','product']
class ProductListSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    # brand=BrandSerializer()
    brand=serializers.StringRelatedField()
    review=ProductReviewSerializer(source='product_reviews',many=True)
    class Meta:
        model = Product
        fields = '__all__'


class BrandListSerializer(serializers.ModelSerializer):
    # product=ProductListSerializer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'
class BrandDetailSerializer(serializers.ModelSerializer):
    product=ProductListSerializer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'