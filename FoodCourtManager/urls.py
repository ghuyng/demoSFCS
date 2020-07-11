from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.FoodCourtView, name = 'food-court-view'),
    path('add/', views.AddStoreView.as_view(), name='foodcourt-manager-view'),
]