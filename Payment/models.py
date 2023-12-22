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
        try:
            return f'{self.product.name} Payment'
        except Exception:
            return f'meow'

    class Meta:
        verbose_name = "Платёжная информация товара"
        verbose_name_plural = "Платёжные информации товаров"
