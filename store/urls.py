from django.urls import path
from . import views
urlpatterns = [
    #path('make-order/', views.makeOrder, name = 'make-order'),
    path('', views.viewStoreList, name = 'store-list'),
    path('<int:store_id>/', views.userStoreView, name = 'user-store-view'),

]