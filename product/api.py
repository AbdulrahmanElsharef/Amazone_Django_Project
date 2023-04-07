from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerializer,ProductDetailSerializer,BrandSerializer
from .models import *
from rest_framework import generics


# @api_view(['GET'])
# def product_list_api(request):
#     products=Product.objects.all()
#     data=ProductSerializer(products,many=True).data[:50]
#     return Response({'data':data})

class BrandListApi(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()[:30]
class ProductListApi(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()[:30]
    
class ProductDetailUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field='slug'