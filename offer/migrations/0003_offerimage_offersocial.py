# Generated by Django 3.0.4 on 2021-01-20 17:43

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_openingtime"),
        ("offer", "0002_offer_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="OfferSocial",
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
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="offer.Offer"
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
        migrations.CreateModel(
            name="OfferImage",
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
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format=None,
                        keep_meta=True,
                        quality=75,
                        size=[480, 350],
                        upload_to="",
                    ),
                ),
                (
                    "img_category",
                    models.CharField(
                        choices=[
                            ("thumbnail", "thumbnail"),
                            ("other", "other"),
                            ("top_slideshow", "slideshow"),
                        ],
                        default="other",
                        max_length=20,
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="offer.Offer"
                    ),
                ),
            ],
            options={
                "db_table": "offer_images",
            },
        ),
    ]
