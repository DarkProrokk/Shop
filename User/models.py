from django.contrib.auth.models import AbstractUser
from django.db import models
from Cart.models import Cart

class CustomUser(AbstractUser):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, verbose_name='Корзина', related_name='user')

    def save(self, *args, **kwargs):
        if not CustomUser.objects.filter(pk=self.pk).exists():
            self.cart = Cart.objects.create()
        super().save(*args, **kwargs)