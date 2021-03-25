# Generated by Django 3.0.4 on 2021-03-22 18:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0013_auto_20210322_1832"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_id",
            field=models.UUIDField(
                default=uuid.UUID("a28a3419-1565-4114-b7b9-b95b8f2cfc9a"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
