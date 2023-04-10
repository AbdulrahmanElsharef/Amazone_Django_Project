from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView

# Create your views here.

class OrderList(ListView):
    model=Order
    def get_queryset(self):
        queryset=Order.objects.filter(user=self.request.user)
        return queryset
    
    
def checkout(request):
    return render (request,'order/checkout.html',{})


class CartList(ListView):
    pass

