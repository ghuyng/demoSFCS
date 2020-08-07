from django.urls import path
from . import views

urlpatterns = [
    #path('', views.viewCart, name = 'notification-page'),
    path('get-notifications/', views.get_notifications, name = 'get-notifications'),
    path('mark-notifications/', views.mark_notifications, name = 'mark-notifications'),
]