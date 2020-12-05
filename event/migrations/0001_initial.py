# Generated by Django 3.0.4 on 2020-12-05 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "0004_guest_musicgenre_venue"),
        ("business", "0001_initial"),
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
                (
                    "genre",
                    models.ManyToManyField(
                        related_name="music", to="common.MusicGenre"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventSetUp",
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
                ("price", models.IntegerField()),
                ("to_be_held", models.DateTimeField(blank=True, null=True)),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.Business",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.Event"
                    ),
                ),
                (
                    "guest",
                    models.ManyToManyField(
                        blank=True, related_name="guest", to="common.Guest"
                    ),
                ),
            ],
        ),
    ]