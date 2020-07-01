from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.

def processPayment(request):
    return True

@login_required
def makeOrder(request):
    if processPayment(request):
        order = request.user.order_set.create()
        return render(request,'order.html', {'order' : order})


@login_required
def viewOrderList(request):
    order_list = request.user.order_set.all()
    return render(request, 'user_orderlist.html', {'order_list': order_list})


@login_required
def viewOrderByID(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order.html', {'order': order})