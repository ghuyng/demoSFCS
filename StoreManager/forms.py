from django.forms import ModelForm
from Food.models import Food

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price', 'imgURL', 'stock']
