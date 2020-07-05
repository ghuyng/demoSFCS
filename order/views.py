from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Order, StoreOrder, OrderItem, Status
from Food.models import Food
from django.contrib.auth.decorators import login_required

# Create your views here.

def processPayment(request):
    return True


def makeOrder(request):
    if 'cart' not in request.session or request.session['cart'] == {}:
        return JsonResponse({"success": False,"message": "EMPTY_CART"})

    if not request.user.is_authenticated:
        return JsonResponse({"success": False, "message": "LOGIN_REQUIRED"})

    if processPayment(request):
        cart = request.session['cart']
        user = request.user
        order = user.order_set.create()
        for food_id, quantity in cart.items():
            food = Food.objects.get(id = int(food_id))
            store_order, created = order.storeorder_set.get_or_create(store=food.store,
                                                                      defaults={'status':Status.PROCESSING})

            store_order.orderitem_set.create(product=food,
                                             paid_price=food.price,
                                             quantity=quantity)

        request.session['cart'] = {}
        return JsonResponse({"success" : True,"message": ""}, status=200)
    else:
        return JsonResponse({"success" : False,"message": "FAIL_PAYMENT"})


@login_required
def viewOrderList(request):
    order_list = request.user.order_set.all().order_by('-date_created')
    return render(request, 'user_orderlist.html', {'order_list': order_list})


@login_required
def viewOrderByID(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    item_list = [order_item for store_order in order.storeorder_set.all()
                for order_item in store_order.orderitem_set.all()]
    status = order.getStatus().label
    total = order.getTotal()
    return render(request, 'order.html', {'order': order,
                                          'item_list' : item_list,
                                          'status' : status,
                                          'total' : total})