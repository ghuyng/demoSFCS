from django.urls import path
from .views import FoodView
from . import views

urlpatterns = [
    path('', FoodView.homepageView),
    path('search/', FoodView.searchByName, name='search_food_by_name'),
    path('food/<int:food_id>/', FoodView.foodInfoView, name='view_food_info'),
    path('contact/', views.contact, name='contact')
]