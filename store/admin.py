from django.contrib import admin
from .models import Store
from Food.models import Food

# Register your models here.

class FoodInLine(admin.TabularInline):
    model = Food
    extra = 1

class StoreAdmin(admin.ModelAdmin):

    inlines = [FoodInLine]

admin.site.register(Store, StoreAdmin)