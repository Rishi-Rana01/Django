from django.shortcuts import render
from .models import Product,Store
from .forms import ProductForm

# Create your views here.
def all(request):
    products = Product.objects.all()
    return render(request, 'apps/all.html', {'products': products})

def app_store_view(request):
    stores= None
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
           product_variety= form.changed_data['product_variety']
           stores=Store.objects.filter(product_variety=product_variety)
    else:
        form = ProductForm()
    return  render(request, 'apps/app_stores.html', {'stores': stores, 'form': form})