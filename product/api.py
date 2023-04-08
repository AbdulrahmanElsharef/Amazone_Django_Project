from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerializer,ProductDetailSerializer,BrandListSerializer,BrandDetailSerializer
from .models import *
from rest_framework import generics
from utils.my_pagination import ProductPagination
from rest_framework import filters


# @api_view(['GET'])
# def product_list_api(request):
#     products=Product.objects.all()
#     data=ProductSerializer(products,many=True).data[:50]
#     return Response({'data':data})


class ProductListApi(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    pagination_class=ProductPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name', 'flag','price']
    ordering_fields = ['flag', 'price','name']
    
class ProductDetailUpdateApi(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field='slug'
    
    
class BrandListApi(generics.ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name',]
    ordering_fields = ['slug',]
    

class BrandDetailUpdateApi(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
    lookup_field='slug'