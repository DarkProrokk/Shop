from django.db import models

from Payment.models import ItemPaymentInfo


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='Родительская категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Mark(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT, verbose_name='Марка')
    count = models.IntegerField(default=0, blank=True, verbose_name='Количество на складе')
    payment = models.OneToOneField(ItemPaymentInfo, on_delete=models.CASCADE, blank=True, related_name="product",
                                   verbose_name="Платёжная информация")

    def __str__(self):
        return self.name

    def payment_price(self):
        return self.payment.price

    def payment_currency(self):
        return self.payment.currency

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Property(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название характеристики")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"


class PropertyValue(models.Model):
    value = models.CharField(max_length=50, verbose_name="Значение характеристики")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="properties", verbose_name="Товар")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="Характеристика")

    def __str__(self):
        return f"{self.property}"

    class Meta:
        verbose_name = "Значение характеристики"
        verbose_name_plural = "Значения характеристик"
