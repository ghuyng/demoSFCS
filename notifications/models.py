from django.db import models

from .signals import store_completed_signal, user_order_completed_signal
from django.dispatch import receiver

from store.models import Store
from order.models import Status, StoreOrder
from django.contrib.auth.models import User
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
    user.notification_set.create(message='Đơn hàng của bạn đã được hoàn tất', url_link=order.id)


class Notification(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length = 256) #message to display
    url_link = models.CharField(max_length = 2000) #link the notification to some page

    READ = 1
    UNREAD = 0
    NOTI_STATUS = [(UNREAD, 'unread'), (READ, 'read')]
    status = models.BooleanField(choices=NOTI_STATUS, default=UNREAD, blank=False)


