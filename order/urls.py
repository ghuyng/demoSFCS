from django.urls import path
from . import views
urlpatterns = [
    path('', views.viewCart, name = 'checkout-cart'),
    path('add-to-cart/', views.addToCart,name = 'add-to-cart'),

]