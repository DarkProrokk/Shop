from django.core.management.base import BaseCommand

from Product.models import *


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arg1', type=int, default=5, nargs='?')

    def handle(self, *args, **options):
        if not Category.objects.filter(name="categoryParent").exists():
            categoryParent = Category.objects.create(name="categoryParent")
            categoryChild = Category.objects.create(name="categoryChild", parent=categoryParent)
        else:
            categoryParent = Category.objects.get(name="categoryParent")
            categoryChild = Category.objects.get(name="categoryChild", parent=categoryParent)
        if not Property.objects.filter(name="TestProperty").exists():
            prop = Property.objects.create(name="TestProperty")
            prop2 = Property.objects.create(name="TestProperty2")
        else:
            prop = Property.objects.get(name="TestProperty")
            prop2 = Property.objects.get(name="TestProperty2")
        arg = options['arg1']
        for i in range(1, arg + 1):
            if Product.objects.filter(name=f"TestProduct{i}").exists():
                continue
            currency = "usd" if i % 2 == 0 else "eur"
            payment = ItemPaymentInfo.objects.create(price=i * 10, currency=currency)
            mark = Mark.objects.create(name=f"TestMark{i}")
            prod = Product.objects.create(
                name=f"TestProduct{i}",
                mark=mark,
                category=categoryChild,
                description="TestDescription",
                payment=payment,
                count=i * 20
            )
            prop_value = PropertyValue.objects.create(value=i * 20, product=prod, property=prop)
            prop_value = PropertyValue.objects.create(value=i * 50, product=prod, property=prop2)
            print(f'{prod.name}' 'created')
