from django.contrib import admin

# Register your models here.
from .models import Category, Mark, Product, Property, PropertyValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', ('category', 'mark', 'payment'), 'description', 'count']
    list_display = ['name', 'category', 'mark', 'description', 'count', 'payment_price', 'payment_currency']
    list_editable = ['category', 'mark', 'count']
    list_per_page = 10



admin.site.register(Category)
admin.site.register(Mark)
admin.site.register(Property)
admin.site.register(PropertyValue)
