# Generated by Django 3.1.2 on 2020-11-08 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bill', '0001_initial'),
        ('shopping_cart', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_cart.shopping_cart'),
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
    ]
