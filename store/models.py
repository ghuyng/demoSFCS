from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tên cửa hàng')
    description = models.TextField(default='',verbose_name='Mô tả')
    store_img = models.CharField(max_length=2000,default='', verbose_name='Ảnh đại diện')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Chủ cửa hàng')

    def __str__(self):
        return self.name