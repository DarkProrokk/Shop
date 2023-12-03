from django.db import models


# Create your models here.


class ItemPaymentInfo(models.Model):
    choices = [
        ('usd', 'USD'),
        ('eur', 'EUR')
    ]

    price = models.FloatField(verbose_name="Цена")
    currency = models.CharField(max_length=50, choices=choices, verbose_name="Валюта")

    def __str__(self):
        return f'{self.product.name} Payment'

    class Meta:
        verbose_name = "Платёжная информация товара"
        verbose_name_plural = "Платёжные информации товаров"
