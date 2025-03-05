from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product, Wishlist, Cart, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'specifications', 'price', 'stock', 'supplier', 'delivery_method', 'category')
    search_fields = ('name', 'description', 'category')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product') 
    search_fields = ('user__username', 'product__name') 

class CartAdmin(admin.ModelAdmin): 
    list_display = ('user', 'product', 'quantity') 
    search_fields = ('user__username', 'product__name') 

class OrderAdmin(admin.ModelAdmin): 
    list_display = ('user', 'product', 'quantity', 'total_price', 'date_ordered') 
    search_fields = ('user__username', 'product__name', 'date_ordered') 

admin.site.register(CustomUser, UserAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Wishlist, WishlistAdmin)

admin.site.register(Cart, CartAdmin)

admin.site.register(Order, OrderAdmin)