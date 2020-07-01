from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Order(models.Model):
    store = models.ForeignKey(
        'store.Store',
        on_delete = models.CASCADE,
        null=True,
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Order ID : {} of user : {} from store : {}'.format(self.id, self.customer.username, self.store)