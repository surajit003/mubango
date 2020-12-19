# Generated by Django 3.0.4 on 2020-12-19 16:34

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
        ("business", "0002_auto_20201219_1403"),
    ]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="address",
            field=address.models.AddressField(
                on_delete=django.db.models.deletion.CASCADE, to="address.Address"
            ),
        ),
    ]
