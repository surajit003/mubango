# Generated by Django 3.0.4 on 2021-01-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0002_auto_20210107_1849"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text="Unique value for product page URL, created from name.",
                max_length=255,
                null=True,
            ),
        ),
    ]
