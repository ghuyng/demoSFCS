from django.db import models
from store.models import Store
from django.urls import reverse

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 255, verbose_name='Tên món ăn')
    price = models.IntegerField(verbose_name='Giá món ăn')
    imgURL = models.CharField(max_length = 2000, verbose_name='Ảnh đại diện')
    stock = models.BooleanField(verbose_name='Tình trạng là còn hàng')
    store = models.ForeignKey(
        Store,
        on_delete = models.CASCADE,
        null = True,
    )

    def __str__(self):
        return '{} from tiệm {}'.format(self.name, self.store)

    def getStock(self):
        return 'Còn hàng'if self.stock else 'Hết hàng'
