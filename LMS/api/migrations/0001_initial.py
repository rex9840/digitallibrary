# Generated by Django 5.0.1 on 2024-01-09 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                ("RoleID", models.IntegerField(primary_key=True, serialize=False)),
                ("RoleName", models.CharField(max_length=50)),
                (
                    "Description",
                    models.CharField(
                        blank=True,
                        help_text="Description of the role and its permisions",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "Role",
                "db_table_comment": "Role and Permissions Table",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "ID",
                    models.IntegerField(
                        help_text="Auto Incremented ID for the user",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "DateCreated",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Date of creation of the user"
                    ),
                ),
                (
                    "UserID",
                    models.IntegerField(
                        help_text="Unique User ID assogned to user for ideentifiacations",
                        unique=True,
                    ),
                ),
                ("Name", models.CharField(help_text="Name of the user", max_length=50)),
                (
                    "Email",
                    models.EmailField(help_text="Email of the user", max_length=254),
                ),
                ("Password", models.CharField(help_text=" Password of the user")),
                (
                    "Address",
                    models.CharField(help_text="Address of the user", max_length=50),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
                (
                    "Role_id",
                    models.ForeignKey(
                        default=2,
                        help_text="Role and perms of the user as defined from ROLE table BY DEAFULT= 2 [STUDENT]",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.role",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
