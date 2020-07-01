from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from Food.models import Food
from django.contrib.auth.decorators import login_required

# Create your views here.

# cart is store in session as a dictionary with key = food_id and value = quantity
# request.session['cart'] = {f_id1: quantity1, f_id2: quantity2,...}
def addToCart(request):
    quantity = int(request.GET['value'])
    food_id = request.GET['food_id']
    data = {
        'success': False,
    }
    if quantity > 0:
        data['success'] = True

        if 'cart' not in request.session or type(request.session['cart']) is not dict:
            request.session['cart'] = {}

        cart = request.session.get('cart', {})
        if food_id in cart:
            cart[food_id] += quantity
        else:
            cart[food_id] = quantity

        request.session['cart'] = cart

    return JsonResponse(data)

def calcTotal(cart_dict):
    #cart_dict = request.session.get('cart', {})
    total = 0
    for food, quantity in cart_dict:
        total += food.price * quantity

    return total


def viewCart(request):
    cart_dict = request.session.get('cart', {})
    cart = []
    total = 0
    for food_id, quantity in cart_dict.items():
        food = Food.objects.get(id=food_id)
        cart.append((food, quantity))
        total += food.price * quantity

    return render(request, 'cart.html', {'cart': cart, 'total' : total})


def removeFromCart(request):
    food_id = request.GET['food_id']
    try:
        cart_dict = request.session['cart']
        if food_id in cart_dict:
            del cart_dict[food_id]
            request.session['cart'] = cart_dict
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)
    except KeyError:
        return JsonResponse({"success": False}, status=400)


def updateItem(request):
    food_id = request.GET['food_id']
    quantity = int(request.GET['value'])
    try:
        cart_dict = request.session['cart']
        if food_id in cart_dict:
            cart_dict[food_id] = quantity
            request.session['cart'] = cart_dict
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)
    except KeyError:
        return JsonResponse({"success": False}, status=400)