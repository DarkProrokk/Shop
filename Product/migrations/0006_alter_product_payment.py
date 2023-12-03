# Generated by Django 4.2.7 on 2023-12-02 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0001_initial'),
        ('Product', '0005_alter_propertyvalue_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='payment',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='Payment.itempaymentinfo'),
        ),
    ]