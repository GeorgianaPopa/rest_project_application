from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, filters  
from rest_framework.permissions import IsAuthenticated, AllowAny 
from .models import Product, Wishlist, Cart, Order
from .serializers import ProductSerializer, WishlistSerializer, CartSerializer, OrderSerializer 
from .permissions import IsAdminUser 
from django.http import JsonResponse

# user
# user@abc.com
# parola1234

def home(request):
    products = Product.objects.all()
    products_by_category = {}

    for product in products:
        if product.category not in products_by_category:
            products_by_category[product.category] = []
        products_by_category[product.category].append(product)

    context = {
        'products_by_category': products_by_category
    }
    return render(request, 'home.html', context)

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout(request):
    if request.method == 'POST':
        Cart.objects.filter(user=request.user).delete()
        return redirect('cart')
    return render(request, 'checkout.html')

class ProductViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    filter_backends = [filters.SearchFilter] 
    search_fields = ['name', 'description', 'category'] 
    
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

class OrderViewSet(viewsets.ModelViewSet): 
    queryset = Order.objects.all() 
    serializer_class = OrderSerializer 
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self): 
        return Order.objects.filter(user=self.request.user)
    
def increase_quantity(request, product_id):
    cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)
    cart_item.quantity += 1
    cart_item.save()
    total_price = cart_item.quantity * cart_item.product.price
    return JsonResponse({'quantity': cart_item.quantity, 'total_price': total_price})

def decrease_quantity(request, product_id):
    cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    total_price = cart_item.quantity * cart_item.product.price
    return JsonResponse({'quantity': cart_item.quantity, 'total_price': total_price})