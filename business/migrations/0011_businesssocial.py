# Generated by Django 3.0.4 on 2021-01-08 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_social"),
        ("business", "0010_auto_20210108_2111"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessSocial",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
                ("active", models.BooleanField(default=False)),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.Business",
                    ),
                ),
                (
                    "social",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="common.Social"
                    ),
                ),
            ],
        ),
    ]
