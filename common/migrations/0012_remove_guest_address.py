# Generated by Django 3.0.4 on 2020-12-19 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0011_auto_20201219_1701"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="guest",
            name="address",
        ),
    ]
