from django.db import models

# Create your models here.
class Delivery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='delivery')
    
class Order(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_details = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)    