from django.contrib import admin

from .models import Product ,ProductReview, Store, ProductCertificate


# Register your models here.
class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'date_added')
    search_fields = ('name', 'description')
    list_filter = ('type', 'date_added')
    inlines = [ProductReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'owner')
    search_fields = ('name', 'location')
    filter_horizontal = ('product_variety',)

class ProductCertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'product', 'issued_date')
    list_filter = ('issued_date',)
    

admin.site.register(Product, ProductAdmin,)
admin.site.register(ProductReview)
admin.site.register(Store, StoreAdmin)
admin.site.register(ProductCertificate, ProductCertificateAdmin)
