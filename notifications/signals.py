from django.dispatch import Signal

store_completed_signal = Signal(providing_args=["store_order"])