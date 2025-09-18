from django.shortcuts import render
from .models import Product

# Create your views here.
def all(request):
    products = Product.objects.all()
    return render(request, 'apps/all.html', {'products': products})