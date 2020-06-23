from django.shortcuts import render
from django.views import View
from .models import Food

# Create your views here.
class FoodView(View):

    def homepageView(request):
        food_list = Food.objects.all()
        return render(request, 'template.html', {'food_list' : food_list})

