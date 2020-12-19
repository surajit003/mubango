# Generated by Django 3.0.4 on 2020-12-19 16:34

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
        ("account", "0003_auto_20201213_1253"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="address",
            field=address.models.AddressField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="address.Address",
            ),
        ),
    ]