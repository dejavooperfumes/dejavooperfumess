# Generated by Django 4.2.3 on 2023-07-23 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0013_rename_product_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='mrp12',
        ),
        migrations.RemoveField(
            model_name='products',
            name='sellingprice12',
        ),
    ]
