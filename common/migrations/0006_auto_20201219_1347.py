# Generated by Django 3.0.4 on 2020-12-19 13:47

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
        ("common", "0005_auto_20201219_1258"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="address",
            field=address.models.AddressField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="address.Address",
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="location",
            field=models.CharField(max_length=100),
        ),
    ]