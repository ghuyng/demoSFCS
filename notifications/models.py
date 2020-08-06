from django.db import models

from .signals import store_completed_signal, user_order_completed_signal
from django.dispatch import receiver

from store.models import Store
from order.models import Status, StoreOrder
# Create your models here.

@receiver(store_completed_signal, sender=Store)
def handler_store_completed(sender, **kwargs):
    store_order = kwargs['store_order']
    if store_order.order.getStatus() == Status.COMPLETED :
        #signal user
        user_order_completed_signal.send(order=store_order.order)


@receiver(user_order_completed_signal)
def handler_user_order_completed(**kwargs):
    order = kwargs['order']
    user = order.customer
    pass
    #user.receive_noti(message)