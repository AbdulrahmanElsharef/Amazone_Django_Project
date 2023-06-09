from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView,DetailView

# Create your views here.

class OrderList(ListView):
    model=Order
    def get_queryset(self):
        queryset=Order.objects.filter(user=self.request.user)
        return queryset
    
def add_to_Cart(request):
    if request.method=='POST':
        product_id=request.POST['productid']
        quantity=request.POST['quantity']
        product=Product.objects.get(id=product_id)
        cart=Cart.objects.get(user=request.user,status='InProgress')
        cart_detail,created=CartDetail.objects.get_or_create(
            cart=cart,
            product=product
        )
        cart_detail.quantity=int(quantity)
        cart_detail.price=product.price
        cart_detail.total=int(quantity)*product.price
        cart_detail.save()
    return redirect(f'/products/{product.slug}')
        


def checkout(request):
    return render (request,'order/checkout.html',{})


class CartList(ListView):
    pass

