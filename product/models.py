from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models  import User
from django . utils import timezone
# Create your models here.
class Brand(models.Model):
    name=models.CharField(_("name"), max_length=50)
    image=models.ImageField(_("image"), upload_to='brand')
    slug=models.SlugField(_("slug"),null=True,blank=True,unique=True)
    #_______________
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Brand, self).save(*args, **kwargs) # Call the real save() method
    #________________
    def __str__(self):
        return str(self.name)
#____________________________________________________________
FLAG_Type=(('New','New'),('Feature','Feature'),('Sale','Sale'))
class Product(models.Model):
    name=models.CharField(_("name"), max_length=150)
    image=models.ImageField(_("image"), upload_to='product_images')
    flag=models.CharField(_("flag"), max_length=50,choices=FLAG_Type)
    price=models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    sku=models.IntegerField(_("serial"))
    subtitle=models.CharField(_("subtitle"), max_length=500)
    descriptions=models.TextField(_("descriptions"),max_length=10000)
    brand=models.ForeignKey(Brand,verbose_name=_("Brand"), on_delete=models.SET_NULL,blank=True,null=True,related_name='product_brand')
    tag=TaggableManager()
    slug=models.SlugField(_("slug"),null=True,blank=True,unique=True)
    #_______________
    def __str__(self):
        return self.name
    #__________________
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs) # Call the real save() method

# ____________________________________________________________
class ProductImage(models.Model):
    product=models.ForeignKey(Product, verbose_name=_("Product"),on_delete=models.CASCADE,related_name='product_images')
    image=models.ImageField(_("image"), upload_to='product_images')
    #________________
    def __str__(self):
        return str(self.product)
    
# ______________________________________________________________
class ProductReview(models.Model):
    user=models.ForeignKey(User, verbose_name=_("User"),on_delete=models.SET_NULL,blank=True,null=True)
    product=models.ForeignKey(Product,verbose_name=_("Product"), on_delete=models.CASCADE,related_name='product_reviews')
    rate=models.IntegerField(_("rate"))
    review=models.TextField(_("review"),max_length=1000)
    date=models.DateTimeField(_("date"), default=timezone.now)
    #________________
    def __str__(self):
        return str(self.product)
    
# __________________________________________________________