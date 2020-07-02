from django.db import models
from Food.models import Food
from store.models import Store
from django.contrib.auth.models import User
import uuid

# Create your models here.

# OrderItem objects stores info about a product
class OrderItem(models.Model):
    store_order = models.ForeignKey(
        'StoreOrder',
        on_delete = models.CASCADE,
        null = True
    )
    product = models.ForeignKey(Food, on_delete = models.CASCADE)
    paid_price = models.IntegerField() # price of product at the time user pay
    quantity = models.IntegerField()

# StoreOrder object consists of many OrderItem objects from the same store
# this type of order is sent and store to its store

class Status(models.IntegerChoices):
    PROCESSING = 0
    COMPLETED = 1


class StoreOrder(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        null=True,
    )
    order = models.ForeignKey('Order', on_delete = models.CASCADE)

    status = models.IntegerField(choices=Status.choices, default=Status.PROCESSING)

    def getTotal(self):
        total = 0
        for order_item in self.orderitem_set.all():
            total += order_item.paid_price * order_item.quantity

        return total

# Order object consists of many StoreOrder objects
# this is the order of user
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def getTotal(self):
        total = 0
        for store_order in self.storeorder_set.all():
            total += store_order.getTotal()

        return total

    # return COMPLETED if all store_order is COMPLETED
    def getStatus(self):
        for store_order in self.storeorder_set.all():
            if store_order.status == Status.PROCESSING:
                return Status.PROCESSING

        return Status.COMPLETED


    def __str__(self):
        return 'Order ID : {} of user : {}'.format(self.id, self.customer.username)