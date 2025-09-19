from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

# One to many relationship with User
class ProductReview(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews') # Basic.txt
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    comment=models.TextField(default='')
    date_added= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review of {self.product.name} by {self.user.username}'
    

# Many to many relationship with User
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    product_variety=models.ManyToManyField(Product, related_name='stores')
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# one to one relationship with User
class ProductCertificate(models.Model):
    product=models.OneToOneField(Product, on_delete=models.CASCADE, related_name='certificate')
    certificate_name=models.CharField(max_length=100)
    issued_date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return f'Certificate for {self.product.name}'
    