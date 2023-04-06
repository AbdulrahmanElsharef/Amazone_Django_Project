from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics


# @api_view(['GET'])
# def product_list_api(request):
#     products=Product.objects.all()
#     data=ProductSerializer(products,many=True).data[:50]
#     return Response({'data':data})

class ProductListApi(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[:30]
    
class ProductDetailUpdateApi(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field='slug'