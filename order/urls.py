from django.urls import path
from .views import CartView
urlpatterns = [
    path('', CartView.viewCart, name = 'checkout-cart'),
    path('add-to-cart/', CartView.addToCart,name = 'add-to-cart'),

]