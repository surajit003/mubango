# Generated by Django 3.0.4 on 2021-01-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0008_businessimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="businessimage",
            name="img_category",
            field=models.CharField(
                choices=[
                    ("thumbnail", "thumbnail"),
                    ("other", "other"),
                    ("top_slideshow", "slideshow"),
                ],
                default="other",
                max_length=20,
            ),
        ),
    ]
