from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    store_img = models.CharField(max_length=2000,default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return self.name