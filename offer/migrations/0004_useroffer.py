# Generated by Django 3.0.4 on 2020-12-19 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("offer", "0003_offer_limit"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserOffer",
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
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="offer.Offer"
                    ),
                ),
                (
                    "user",
                    models.ManyToManyField(
                        related_name="users", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "UserOffer",
            },
        ),
    ]