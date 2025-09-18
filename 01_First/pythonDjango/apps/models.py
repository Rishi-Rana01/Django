from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPE_CHOICES =[
        ('El', 'Electronics'),
        ('Cl', 'Clothing'),
        ('Bo', 'Books'),
        ('Ho', 'Home'),
        ('Ot', 'Other'),
    ]
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to='products/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=PRODUCT_TYPE_CHOICES, default='Ot')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

