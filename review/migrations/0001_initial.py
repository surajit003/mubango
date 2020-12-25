# Generated by Django 3.0.4 on 2020-12-25 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("business", "0004_auto_20201219_1701"),
        ("common", "0012_remove_guest_address"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("date_last_modified", models.DateField(auto_now=True)),
                ("date_added", models.DateField(auto_now=True)),
                ("comment", models.TextField()),
                (
                    "experience",
                    models.CharField(
                        choices=[
                            ("positive", "Positive"),
                            ("neutral", "Neutral"),
                            ("negative", "Negative"),
                        ],
                        default="neutral",
                        max_length=20,
                    ),
                ),
                ("images", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.Business",
                    ),
                ),
                (
                    "rating",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="common.Rating"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Reviews",
            },
        ),
    ]
