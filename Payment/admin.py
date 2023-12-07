from django.contrib import admin

from .models import ItemPaymentInfo

class ItemPaymentInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(ItemPaymentInfo, ItemPaymentInfoAdmin)

#todo create custom admin for Payment