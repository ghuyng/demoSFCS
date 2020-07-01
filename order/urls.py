from django.urls import path
from . import views
urlpatterns = [
    path('make-order/', views.makeOrder, name = 'make-order'),
    path('', views.viewOrderList, name = 'order-list'),
    path('<uuid:order_id>/', views.viewOrderByID, name = 'view-order'),
]