# Generated by Django 3.0.4 on 2021-03-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0017_remove_business_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="business",
            name="price_type",
        ),
    ]
