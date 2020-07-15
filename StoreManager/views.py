from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, Http404
from store.models import Store
from Food.models import Food
from FoodCourtManager.forms import StoreForm
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def ManageStoreView(request):
    if request.user.has_perm('Food.add_food'):
        store_list = Store.objects.all()
        context = {'store_list': store_list}
        return render(request, 'storelist_managerview.html', context)
    else:
        return HttpResponse('Bạn không có quyền thực hiện chức năng này')

def ManageStore(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    menu = [food for food in store.food_set.all()]

    return render(request, 'editstore_managerview.html', {'store': store, 'menu': menu})

def UpdateStore(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    form = StoreForm(instance=store)

    if request.method == 'POST':
        store = get_object_or_404(Store, id=store_id)
        form = StoreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            store_img = form.cleaned_data.get('store_img')

            store.name = name
            store.description = description
            store.store_img = store_img
            store.save()
            return HttpResponseRedirect("/storemanager")

    return render(request, 'updatestore_managerview.html', {'form': form})
