# Generated by Django 3.0.4 on 2021-01-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0005_auto_20210108_1217"),
    ]

    operations = [
        migrations.AddField(
            model_name="business",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]