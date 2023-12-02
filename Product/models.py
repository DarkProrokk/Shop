from django.db import models

from Payment.models import ItemPaymentInfo


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Mark(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
    count = models.IntegerField(default=0, blank=True)
    payment = models.OneToOneField(ItemPaymentInfo, on_delete=models.CASCADE, blank=True, related_name="payment")

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PropertyValue(models.Model):
    value = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="properties")
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.property}"
