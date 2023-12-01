from django.db.models.signals import (post_save)
from django.dispatch import receiver
from .models import Shift
from orders.views import OrderViewSet

@receiver(post_save, sender=Shift)
def restart_order_counter(sender, instance, **kwargs):
    print("*"*10)
    print("Shift signals")
    # reset the order counter whith each shift object instantaiting
    OrderViewSet.is_first_in_the_shift = True

    