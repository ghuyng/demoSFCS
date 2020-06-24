from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Food

# Create your views here.
class FoodView(View):

    def homepageView(request):
        food_list = Food.objects.all()
        return render(request, 'template.html', {'food_list' : food_list})

    def searchByName(request):
        result = Food.objects.filter(name__contains=request.GET['food_name'])
        return render(request, 'search_page.html', {'food_list' : result})

    def foodInfoView(request, food_id):
        food = get_object_or_404(Food, id=food_id)
        return render(request, 'food_page.html', {'food': food})

    def addToCart(request):
        quantity = int(request.GET['value'])
        food_id = int(request.GET['food_id'])
        data = {
            'success' : False,
            'value' : quantity
        }
        if quantity > 0:
            data['success'] = True
            request.session[food_id] = quantity
            data['value'] = request.session[food_id]

        return JsonResponse(data)

    def viewCart(request):
        #if not request.session[1]:
        request.session[1] = '10'
        return render(request, 'cart.html', {'cart': request.session[1]})



