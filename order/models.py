from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils import timezone
from product.models import Product
from utils.generate_code import generate_code
# Create your models here.

CART_STATUS = (('InProgress', 'InProgress'), ('Completed', 'CompleteD'))


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "user_cart"), related_name='user_cart', on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(_("status"), max_length=20, choices=CART_STATUS)

    def __str__(self):
        return str(self.user)


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_(
        "cart_detail"), related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_(
        "product_cart"), related_name='product_cart', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(_("quantity"),null=True,blank=True)
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2,null=True,blank=True)
    total = models.DecimalField(_("total"), max_digits=5, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return str(self.cart)


ORDER_STATUS = (('Received', 'Received'), ('Processed', 'Processed'),
                ('Shipped', 'Shipped'), ('Delivered', 'Delivered'))


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "user_order"), related_name='user_order', on_delete=models.SET_NULL, blank=True, null=True)
    code = models.CharField(_("code"), max_length=10, default=generate_code)
    status = models.CharField(_("status"), max_length=20, choices=ORDER_STATUS)
    order_time = models.DateTimeField(_("order_time"), default=timezone.now)
    delivery_time = models.DateTimeField(
        _("delivery_time"), blank=True, null=True)

    def __str__(self):
        return self.code


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_(
        "order_detail"), related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_(
        "product_order"), related_name='product_order', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(_("quantity"))
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.order)


class Coupon(models.Model):
    code=models.CharField(_("code"), max_length=30)
    value=models.DecimalField(_("value"), max_digits=5, decimal_places=2)
    from_date=models.DateField(_("from_date"), default=timezone.now)
    to_date=models.DateField(_("from_date"), default=timezone.now)
    quantity=models.IntegerField(_("quantity"))
    image=models.ImageField( upload_to='coupon/',null=True,blank=True)
    
    def __str__(self):
        return self.code
    