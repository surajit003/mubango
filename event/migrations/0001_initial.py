# Generated by Django 3.0.4 on 2021-01-02 20:27

import address.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("business", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("address", "0003_auto_20200830_1851"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("priority_level", models.IntegerField(default=0)),
                ("to_be_held_on", models.DateTimeField()),
                ("active", models.BooleanField(default=False)),
                ("is_special", models.BooleanField(default=False)),
                ("num_of_tickets", models.IntegerField(default=0)),
                (
                    "business",
                    models.ManyToManyField(
                        related_name="business", to="business.Business"
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        blank=True, related_name="music", to="common.MusicGenre"
                    ),
                ),
                (
                    "guest",
                    models.ManyToManyField(
                        blank=True, related_name="guest", to="common.Guest"
                    ),
                ),
                (
                    "location",
                    address.models.AddressField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="address.Address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventUser",
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
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.Event"
                    ),
                ),
                (
                    "visitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Event User",
            },
        ),
    ]
