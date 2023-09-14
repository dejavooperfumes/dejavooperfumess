# Generated by Django 4.2.3 on 2023-07-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0007_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='feeback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]