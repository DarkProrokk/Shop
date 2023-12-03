from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from Cart.models import Cart


class CustomUser(AbstractUser):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, verbose_name='Корзина', related_name='user')
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        if not CustomUser.objects.filter(pk=self.pk).exists():
            self.cart = Cart.objects.create()
        super().save(*args, **kwargs)
