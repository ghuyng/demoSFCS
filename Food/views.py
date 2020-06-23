from django.shortcuts import render
from django.views import View
from .models import Food

# Create your views here.
class FoodView(View):

    def homepageView(request):
        food_list = Food.objects.all()
        return render(request, 'template.html', {'food_list' : food_list})

    def searchByName(request):
        result = Food.objects.filter(name__contains=request.GET['food_name'])
        return render(request, 'search_page.html', {'food_list' : result})

    def viewFoodInfo(request, food_id):
        food = Food.objects.get(id=food_id)
        return render(request, 'food_page.html', {'food': food})

