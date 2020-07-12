from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, Http404
from store.models import Store
from .forms import StoreForm
from django.views.generic import DeleteView, DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def FoodCourtView(request):
    if request.user.has_perm('store.add_store'):
        store_list = Store.objects.all()
        context = {'store_list': store_list}
        return render(request, 'foodcourt_managerview.html', context)
    else:
        return HttpResponse('Bạn không có quyền thực hiện chức năng này')

class AddStoreView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        Form = StoreForm()
        return render(request, 'addstore_managerview.html', {'Form':Form})

    def post(self, request):
        Form = StoreForm(request.POST)
        if not Form.is_valid():
            return HttpResponse('Nhập sai dữ liệu')
        if request.user.has_perm('store.add_store'):
            Form.save()
        else:
            return HttpResponse('Bạn không có quyền thực hiện chức năng này')
        return HttpResponse('Thêm mới thành công')
        #return HttpResponseRedirect(reverse('foodcourtmanager:food-court-view'))

class DeleteStoreView(LoginRequiredMixin,DeleteView):
    template_name = 'deletestore_managerview.html'
    login_url = '/accounts/login/'

    def get_object(self):
        if self.request.user.has_perm('store.delete_store'):
            id_ = self.kwargs.get("id")
            return get_object_or_404(Store, id=id_)
        else:
            raise Http404("Bạn không có quyền thực hiện chức năng này.")

    def get_success_url(self):
        return reverse('foodcourtmanager:food-court-view')