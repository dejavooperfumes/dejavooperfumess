# Generated by Django 4.2.3 on 2023-07-21 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0011_product_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mrp12',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='sellingprice12',
            field=models.CharField(default='', max_length=10),
        ),
    ]