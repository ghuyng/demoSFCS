from django.urls import path
from .views import FoodView
urlpatterns = [
    path('', FoodView.homepageView),
    path('search/', FoodView.searchByName, name='urlname')
]