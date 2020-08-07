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

def contact(request):
    return render(request,'contact.html')





