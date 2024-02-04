from django.contrib import admin
from .models import Product, ProductImage
# Register your models here.

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)