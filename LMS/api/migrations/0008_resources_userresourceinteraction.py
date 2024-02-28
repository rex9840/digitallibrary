# Generated by Django 5.0.1 on 2024-02-28 08:50

import api.resources.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_users_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resources",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=500)),
                (
                    "Resource_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=api.resources.models.Resources.get_profile_pic_filename,
                    ),
                ),
                (
                    "Resource_file",
                    models.FileField(
                        blank=True, null=True, upload_to="upload/resource_file"
                    ),
                ),
            ],
            options={
                "db_table": "Resources",
            },
        ),
        migrations.CreateModel(
            name="UserResourceInteraction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Rating",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(5)],
                    ),
                ),
                ("Comment", models.CharField(blank=True, max_length=500, null=True)),
                ("Downloaded", models.BooleanField(default=False)),
                ("likes", models.IntegerField(default=0)),
                ("dislikes", models.IntegerField(default=0)),
                (
                    "resource_id",
                    models.ForeignKey(
                        db_column="resource_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="api.resources",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "UserResourceInteraction",
            },
        ),
    ]