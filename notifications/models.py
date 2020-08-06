from django.db import models


from store.models import Store
from order.models import Status, StoreOrder
from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length = 256) #message to display
    url_link = models.CharField(max_length = 2000) #link the notification to some page

    READ = 1
    UNREAD = 0
    NOTI_STATUS = [(UNREAD, 'unread'), (READ, 'read')]
    status = models.BooleanField(choices=NOTI_STATUS, default=UNREAD, blank=False)


