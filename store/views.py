from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Store
from FoodCourtManager.forms import StoreForm


# Create your views here.

def viewStoreList(request):
    store_list = Store.objects.all()
    return render(request, 'store_list.html', {'store_list': store_list})


def userStoreView(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    menu = [food for food in store.food_set.all()]

    return render(request, 'store_userview.html', {'store': store, 'menu' : menu})

