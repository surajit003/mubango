# Generated by Django 3.0.4 on 2021-01-13 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
        ("account", "0004_remove_profile_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="address.Address",
            ),
        ),
    ]
