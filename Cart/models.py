from django.db import models

from Product.models import Product


# Create your models here.


class Cart(models.Model):
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="products", verbose_name="Корзина")
    quantity = models.IntegerField(verbose_name="Количество")
    product = models.ForeignKey('Product.Product', on_delete=models.CASCADE, verbose_name="Товар")

    def save(self, *args, **kwargs):
        prod = Product.objects.filter(pk=self.product.id).first()
        if prod:
            item = CartItem.objects.filter(cart=self.cart, product=prod).exists()
            if CartItem.objects.filter(pk=self.pk).exists():
                self.quantity -= CartItem.objects.filter(pk=self.pk).first().quantity
            if prod.count >= self.quantity:
                if not item:
                    super(CartItem, self).save()
                else:
                    cart = CartItem.objects.get(product=prod)
                    cart.quantity += self.quantity
                    super(CartItem, cart).save()
                prod.count -= self.quantity
                prod.save()
            else:
                raise ValueError(f"Добавляемое значение({self.quantity}) должно быть меньше и равно количеству"
                                 f" товаров({prod.count})")
        else:
            raise ValueError(f"Товара {prod} не существует")

    def __str__(self):
        return f'{self.product.name} ---- {self.quantity}'

    class Meta:
        verbose_name = "Предмет в корзине"
        verbose_name_plural = "Предметы в корзинах"
