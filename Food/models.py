from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    imgURL = models.CharField(max_length = 2000)
    stock = models.BooleanField()

    def __str__(self):
        return self.name

    def getStock(self):
        return 'Còn hàng'if self.stock else 'Hết hàng'
