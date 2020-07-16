from django.forms import ModelForm
from Food.models import Food
from store.models import Store

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price', 'imgURL', 'stock']

class StoreOwnerForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'store_img']