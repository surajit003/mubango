# Generated by Django 3.0.4 on 2020-12-19 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0002_auto_20201219_1403"),
        ("offer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="business",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="business.Business"
            ),
        ),
    ]