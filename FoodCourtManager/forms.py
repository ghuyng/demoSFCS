from django.forms import ModelForm
from store.models import Store

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'store_img', 'owner']
