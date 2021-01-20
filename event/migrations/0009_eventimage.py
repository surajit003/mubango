# Generated by Django 3.0.4 on 2021-01-10 16:10

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0012_business_openning_times"),
        ("event", "0008_auto_20210110_1556"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventImage",
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
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.Business",
                    ),
                ),
            ],
            options={
                "db_table": "event_images",
            },
        ),
    ]