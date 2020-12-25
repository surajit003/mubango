# Generated by Django 3.0.4 on 2020-12-25 10:47

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
        ("offer", "0002_offer_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="location",
            field=address.models.AddressField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="address.Address",
            ),
            preserve_default=False,
        ),
    ]