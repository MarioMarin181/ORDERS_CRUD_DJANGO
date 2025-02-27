# Generated by Django 4.2.6 on 2025-02-19 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('orders', '0003_alter_ordermodel_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.ordermodel', verbose_name='Pedido'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clientmodel', verbose_name='Cliente'),
        ),
    ]
