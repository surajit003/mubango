# Generated by Django 3.0.4 on 2021-01-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_openingtime"),
        ("business", "0011_businesssocial"),
    ]

    operations = [
        migrations.AddField(
            model_name="business",
            name="openning_times",
            field=models.ManyToManyField(to="common.OpeningTime"),
        ),
    ]