# Generated by Django 4.2.6 on 2025-02-17 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductModel',
        ),
    ]
