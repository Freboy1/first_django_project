from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')