from django.core.management.base import BaseCommand

from Product.models import *

cat_byt = ['Чайники', 'Микроволновки', 'Миксеры', 'Холодильники']
cat_ele = ['Видеокарты', 'Процессоры']
prod_byt = ['Чайник', 'Микроволновка', 'Миксер', 'Холодильник']
prod_ele = ['Видеокарта', 'Процессор']


def get_byt():
    return cat_byt, prod_byt


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arg1', type=int, default=5, nargs='?')

    def handle(self, *args, **options):
        categoryByt = Category.objects.get_or_create(name="Бытовая техника")[0]
        categoryEle = Category.objects.get_or_create(name="Комплектующие для компьютера")[0]
        for i in cat_byt:
            Category.objects.create(name=i, parent=categoryByt)
        for i in cat_ele:
            Category.objects.create(name=i, parent=categoryByt)
        prop = Property.objects.get_or_create(name="Вес")[0]
        prop2 = Property.objects.get_or_create(name="Объём")[0]
        arg = options['arg1']
        markLG = Mark.objects.get_or_create(name=f"LG")[0]
        markSONY = Mark.objects.get_or_create(name='Sony')[0]

        def create(cat, prod_lst):
            for index in range(len(cat)):
                for i in range(1, arg + 1):
                    currency = "usd" if i % 2 == 0 else "eur"
                    mark = markLG if i % 2 == 0 else markSONY
                    payment = ItemPaymentInfo.objects.create(price=i * 10, currency=currency)
                    prod = Product.objects.create(
                        name=f"{prod_lst[index]} {i}",
                        mark=mark,
                        category=Category.objects.get(name=cat[index]),
                        description="TestDescriptionTestDescriptionTestDescriptionTestDescriptionTestDescription"
                                    "TestDescriptionTestDescription",
                        payment=payment,
                        count=i * 20
                    )
                    PropertyValue.objects.create(value=i * 20, product=prod, property=prop)
                    PropertyValue.objects.create(value=i * 50, product=prod, property=prop2)
                    print(f'{prod.name}' + ' ' + 'created')

        create(cat_byt, prod_byt)
        create(cat_ele, prod_ele)
