from django.db import models


# Create your models here.


class Cart(models.Model):
    products = models.ManyToManyField('Product.Product', blank=True)

    def __str__(self):
        return self.user.username
