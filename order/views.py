from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from Food.models import Food

# Create your views here.

class CartView(View):

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


    def viewCart(request):
        cart_dict = request.session.get('cart', {})
        cart = []
        for food_id, quantity in cart_dict.items():
            cart.append((Food.objects.get(id=food_id), quantity))

        return render(request, 'cart.html', {'cart': cart})


    def clearCart(request):
        try:
           del request.session['cart']
        except KeyError:
            pass
