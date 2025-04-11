from django.urls import path
from .views import home, cart_view, checkout, add_to_cart, increase_quantity, decrease_quantity, predictive_search, product_detail
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('increase_quantity/<int:product_id>/', increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
    path('predictive_search/', predictive_search, name='predictive_search'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('specs_search/', views.specs_search, name='search_specs'),
]