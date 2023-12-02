from django.contrib import admin

# Register your models here.
from .models import Category, Mark, Product, Property, PropertyValue

admin.site.register(Category)
admin.site.register(Mark)
admin.site.register(Product)
admin.site.register(Property)
admin.site.register(PropertyValue)
