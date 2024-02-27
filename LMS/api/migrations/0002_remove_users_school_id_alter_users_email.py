# Generated by Django 5.0.1 on 2024-02-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="users",
            name="school_id",
        ),
        migrations.AlterField(
            model_name="users",
            name="email",
            field=models.EmailField(
                max_length=254,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="email",
            ),
        ),
    ]