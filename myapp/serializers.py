from rest_framework import serializers
from .models import Product, Wishlist, Cart, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Wishlist 
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Order 
        fields = '__all__'
