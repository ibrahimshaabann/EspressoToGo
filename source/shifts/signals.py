from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Shift


@receiver(pre_save, sender=Shift)
def restart_order_counter(sender, instance, **kwargs):
    # if instance.pk == None:
        
        # from orders.views import OrderViewSet
        
        # reset the order counter whith each shift object instantaiting
        # OrderViewSet().is_order_first_in_the_shift = True
        
    from orders.views import OrderViewSet

    # reset the order counter whith each shift object instantaiting
    OrderViewSet().is_order_first_in_the_shift = True
    
    