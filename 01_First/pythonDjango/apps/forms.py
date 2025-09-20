from django import forms
from .models import Product

class ProductForm(forms.Form):
    product_variety = forms.ModelChoiceField(queryset=Product.objects.all(), label="Select Product Varity")