from django.db import models
from store.models import Store

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    imgURL = models.CharField(max_length = 2000)
    stock = models.BooleanField()
    store = models.ForeignKey(
        Store,
        on_delete = models.CASCADE,
        null = True,
    )

    def __str__(self):
        return '{} from tiệm {}'.format(self.name, self.store)

    def getStock(self):
        return 'Còn hàng'if self.stock else 'Hết hàng'
