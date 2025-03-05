from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=5, choices=ROLES)  

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    specifications = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    supplier = models.CharField(max_length=100)
    delivery_method = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200, blank=True, null=True)  

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 

    class Meta:
        unique_together = ('user', 'product')  

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.quantity}"

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField()  
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  
    date_ordered = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"