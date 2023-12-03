from django.core.management.base import BaseCommand

from Product.models import *


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arg1', type=int, default=5, nargs='?')

    def handle(self, *args, **options):
        categoryParent = Category.objects.get_or_create(name="Бытовая техника")[0]

        categoryChild = Category.objects.get_or_create(name="Холодильники", parent=categoryParent)[0]
        prop = Property.objects.get_or_create(name="Вес")[0]
        prop2 = Property.objects.get_or_create(name="Объём")[0]
        arg = options['arg1']
        mark = Mark.objects.get_or_create(name=f"LG")[0]
        for i in range(1, arg + 1):
            if Product.objects.filter(name=f"Холодильник{i}").exists():
                continue
            currency = "usd" if i % 2 == 0 else "eur"
            payment = ItemPaymentInfo.objects.create(price=i * 10, currency=currency)
            prod = Product.objects.create(
                name=f"Холодильник {i}",
                mark=mark,
                category=categoryChild,
                description="TestDescriptionTestDescriptionTestDescriptionTestDescriptionTestDescription"
                            "TestDescriptionTestDescription",
                payment=payment,
                count=i * 20
            )
            prop_value = PropertyValue.objects.create(value=i * 20, product=prod, property=prop)
            prop_value = PropertyValue.objects.create(value=i * 50, product=prod, property=prop2)
            print(f'{prod.name}'+' ' + 'created')
