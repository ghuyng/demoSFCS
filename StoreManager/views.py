from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, Http404
from store.models import Store
from Food.models import Food
from .forms import FoodForm, StoreOwnerForm
from django.urls import reverse
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def ManageStoreView(request):
    if request.user.has_perm('Food.add_food'):
        store_list = request.user.store_set.all()
        context = {'store_list': store_list}
        return render(request, 'storelist_managerview.html', context)
    else:
        return HttpResponse('Bạn không có quyền thực hiện chức năng này')

@login_required(login_url='/accounts/login/')
def ManageStore(request, store_id):
    store = get_object_or_404(request.user.store_set.all(), id=store_id)
    return render(request, 'store_managerview.html', {'store': store})

@login_required(login_url='/accounts/login/')
def ManageStoreMenu(request, store_id):
    store = get_object_or_404(request.user.store_set.all(), id=store_id)
    menu = [food for food in store.food_set.all()]

    return render(request, 'editmenu_managerview.html', {'store': store, 'menu': menu})

@login_required(login_url='/accounts/login/')
def UpdateStore(request, store_id):
    store = get_object_or_404(request.user.store_set.all(), id=store_id)
    form = StoreOwnerForm(instance=store)

    if request.method == 'POST':
        store = get_object_or_404(request.user.store_set.all(), id=store_id)
        form = StoreOwnerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            store_img = form.cleaned_data.get('store_img')

            store.name = name
            store.description = description
            store.store_img = store_img
            store.save()
            return HttpResponseRedirect("/storemanager")

    return render(request, 'update_managerview.html', {'form': form})

@login_required(login_url='/accounts/login/')
def UpdateFood(request, food_id, store_id):
    food = get_object_or_404(Food, id=food_id)
    form = FoodForm(instance=food)

    if request.method == 'POST':
        food = get_object_or_404(Food, id=food_id)
        form = FoodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            imgURL = form.cleaned_data.get('imgURL')
            stock = form.cleaned_data.get('stock')

            food.name = name
            food.price = price
            food.imgURL = imgURL
            food.stock = stock
            food.save()
            return HttpResponseRedirect(reverse('storemanager:edit-store', args=(store_id,)))

    return render(request, 'update_managerview.html', {'form': form})

@login_required(login_url='/accounts/login/')
def AddFood(request, store_id):
    form = FoodForm()
    store = get_object_or_404(request.user.store_set.all(), id=store_id)

    if request.method == 'POST':
        store = get_object_or_404(Store, id=store_id)
        form = FoodForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.store = store
            instance.save()
            return HttpResponseRedirect(reverse('storemanager:edit-menu', args=(store_id,)))

    return render(request, 'addfood_managerview.html', {'form': form, 'store': store})

#@login_required(login_url='/accounts/login/')
class DeleteFood(DeleteView):
    template_name = 'deletefood_managerview.html'

    def get_object(self):
        if self.request.user.has_perm('Food.delete_food'):
            store_id = self.kwargs.get("store_id")
            food_id = self.kwargs.get("food_id")
            store =  get_object_or_404(self.request.user.store_set.all(), id=store_id)
            return get_object_or_404(store.food_set.all(), id=food_id)
        else:
            raise Http404("Bạn không có quyền thực hiện chức năng này.")

    def get_success_url(self):
        store_id = self.kwargs.get("store_id")
        return reverse('storemanager:edit-menu', args=(store_id,))


@login_required(login_url='/accounts/login/')
def get_store_order(request, store_id):
    #group = Group.objects.get(name='store_owner')
    #if group in request.user.groups.all():
    if request.user.has_perm('Food.delete_food'):
        store = get_object_or_404(request.user.store_set.all(), id=store_id)
        completed_orders = store.storeorder_set.filter(status='C')
        completed_orders = list(zip(completed_orders, [order.orderitem_set.all() for order in completed_orders]))
        processing_orders = store.storeorder_set.filter(status='P')
        processing_orders = list(zip(processing_orders, [order.orderitem_set.all() for order in processing_orders]))
        return render(request, 'order_managerview.html', {'completed_orders' : completed_orders,
                                                          'processing_orders' : processing_orders,})

    else:
        raise Http404("Bạn không có quyền thực hiện chức năng này")