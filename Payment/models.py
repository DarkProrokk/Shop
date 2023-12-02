from django.db import models


# Create your models here.


class ItemPaymentInfo(models.Model):
    choices = [
        ('usd', 'USD'),
        ('eur', 'EUR')
    ]

    price = models.FloatField()
    currency = models.CharField(max_length=50, choices=choices)

    def __str__(self):
        return f'{self.product.name} Payment'
