from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'foodcourtmanager'
urlpatterns = [
    path('', views.FoodCourtView, name='food-court-view'),
    path('add/', views.AddStoreView.as_view(), name='add-food-court'),
    path('<int:id>/delete/', views.DeleteStoreView.as_view(), name='delete-food-court'),
    path('report/', views.GetReport, name='report-view'),
]