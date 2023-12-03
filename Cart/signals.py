from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from Product.models import Product
from .models import CartItem


@receiver(post_save, sender=CartItem)
def delete_cart(sender, instance: CartItem, **kwargs):
    if instance.quantity == 0:
        instance.delete()