from django.urls import path
from .views import FoodView
urlpatterns = [
    path('', FoodView.homepageView),
]