from django.db import models

from .signals import store_completed_signal
from django.dispatch import receiver

from store.models import Store
# Create your models here.

@receiver(store_completed_signal, sender=Store)
def handler_store_completed(sender, **kwargs):
    pass