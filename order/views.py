from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Order, StoreOrder, OrderItem, Status
from django.contrib.auth.decorators import login_required

# Create your views here.

def processPayment(request):
    return True

@login_required
def makeOrder(request):
    if processPayment(request):
        cart = request.session['cart']
        user = request.user
        order = user.order_set.create()
        for food_id, quantity in cart.items():
            food = Food.objects.get(id = int(food_id))
            store_order = order.storeorder_set.get(store=food.store)
            if store_order is None:
                store_order = order.storeorder_set.create(store=food.store,
                                                          status=Status.PROCESSING)

            store_order.orderitem_set.create(product=food,
                                             paid_price=food.price,
                                             quantity=quantity)

        return render(request,'order.html', {'order' : order})


@login_required
def viewOrderList(request):
    order_list = request.user.order_set.all()
    return render(request, 'user_orderlist.html', {'order_list': order_list})


@login_required
def viewOrderByID(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order.html', {'order': order})