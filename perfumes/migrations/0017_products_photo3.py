# Generated by Django 4.2.3 on 2023-08-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0016_review_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='photo3',
            field=models.ImageField(default='All', upload_to='product/'),
        ),
    ]
