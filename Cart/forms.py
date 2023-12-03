from django import forms

from Product.models import Product
from .models import CartItem


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'cart']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['product'].disabled = True
            self.fields['cart'].disabled = True

    def clean_product(self):
        product = self.cleaned_data['product']
        if not product.pk:
            raise forms.ValidationError(f"Товара {product} не существует")
        return product

    def clean_cart(self):
        cart = self.cleaned_data['cart']
        if not cart.pk:
            raise forms.ValidationError(f"Корзина {cart} не существует")
        return cart

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['product']
        if product.count < quantity:
            raise forms.ValidationError(f"Добавляемое значение({quantity}) должно быть меньше и равно количеству"
                                        f" товаров({Product.objects.get(pk=product.id).count})")
        return quantity
