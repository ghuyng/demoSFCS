from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'storemanager'
urlpatterns = [
    path('', views.ManageStoreView, name='manage-store-view'),
    path('<int:store_id>/', views.ManageStore, name='edit-store'),
    path('<int:store_id>/update/', views.UpdateStore, name='update-store'),
    path('<int:store_id>/add/', views.AddFood, name='add-food'),
    path('<int:store_id>/edit/<int:food_id>/update/', views.UpdateFood, name='update-food'),
    path('<int:store_id>/edit/<int:food_id>/delete/', views.DeleteFood.as_view(), name='delete-food'),
]