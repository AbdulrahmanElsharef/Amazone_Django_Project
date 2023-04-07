from rest_framework import serializers
from .models import Product,Brand,ProductReview

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class ProductReviewSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model = ProductReview
        fields = '__all__'
class ProductListSerializer(serializers.ModelSerializer):
    # brand=BrandSerializer()
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