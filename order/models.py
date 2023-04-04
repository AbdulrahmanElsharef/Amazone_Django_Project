from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils import timezone
from product.models import Product
# Create your models here.
ORDER_STATUS=(('Received','Received'),('Processed','Processed'),('Shipped','Shipped'),('Delivered','Delivered'))

class Order(models.Model):
    user=models.ForeignKey(User, verbose_name=_("user_order"),related_name='user_order', on_delete=models.SET_NULL,blank=True,null=True)
    code=models.CharField(_("code"), max_length=15)
    status=models.CharField(_("status"), max_length=20,choices=ORDER_STATUS)
    order_time=models.DateTimeField(_("order_time"),default=timezone.now)
    delivery_time=models.DateTimeField(_("delivery_time"), blank=True,null=True)
    
    def __str__(self):
        return self.code
    
class OrderDetail(models.Model):
    order=models.ForeignKey(Order, verbose_name=_("order_detail"),related_name='order_detail', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, verbose_name=_("product_order"),related_name='product_order', on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(_("quantity"))
    price=models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    
    def __str__(self):
        return str(self.order)
    