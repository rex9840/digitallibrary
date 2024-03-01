# Generated by Django 5.0.2 on 2024-03-01 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_userresourceinteraction_dislikes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresourceinteraction',
            name='resource_id',
            field=models.ForeignKey(db_column='resource_id', on_delete=django.db.models.deletion.CASCADE, to='api.resources'),
        ),
    ]