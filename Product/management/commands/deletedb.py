from django.core.management.base import BaseCommand
from Product.models import *



class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Mark.objects.all().delete()
        ItemPaymentInfo.objects.all().delete()
        Category.objects.all().delete()
        Property.objects.all().delete()