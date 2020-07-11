from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from store.models import Store
from .forms import StoreForm

# Create your views here.
def FoodCourtView(request):
    store_list = Store.objects.all()
    return render(request, 'foodcourt_managerview.html', {'store_list': store_list})

class AddStoreView(View):
    def get(self, request):
        Form = StoreForm()
        return render(request,'addstore_managerview.html',{'Form':Form})

    def post(self, request):
        Form = StoreForm(request.POST)
        if not Form.is_valid():
            return HttpResponse('Nhập sai dữ liệu')
        if request.user.has_perm('store.add_store'):
            Form.save()
        else:
            return HttpResponse('Bạn không thực hiện được tác vụ này')
        return HttpResponse('Đã thêm mới cửa hàng')