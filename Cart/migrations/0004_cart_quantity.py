# Generated by Django 4.2.7 on 2023-12-02 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0003_alter_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]