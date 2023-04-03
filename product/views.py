from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.views.generic import ListView,DetailView
from .forms import ProductReviewForm

class BrandList(ListView):
    model=Brand
    paginate_by=20
    extra_context={'objects_count':Brand.objects.all().count()}

class BrandDetail(ListView):
    model=Product
    template_name = 'product/brand_detail.html'
    paginate_by=10
    extra_context={'objects_count':Product.objects.all().count()}
    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] =Brand.objects.get(slug=self.kwargs['slug'])
        return context


class ProductList(ListView):
    model=Product
    paginate_by=30
    extra_context={'objects_count':Product.objects.all().count()}
    
class ProductDetail(DetailView):
    model=Product
    
    def get_context_data(self, **kwargs):
        product=self.get_object()
        context = super().get_context_data(**kwargs)
        context["related"] =Product.objects.filter(brand=product.brand)[:8]
        return context
    
    
def add_review(request,slug):
    product=Product.objects.get(slug=slug)
    if request.method=='POST':
        form=ProductReviewForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.product=product
            myform.save()
    return redirect(f'/products/{product.slug}')
