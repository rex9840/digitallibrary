# Generated by Django 5.0.3 on 2024-04-08 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_users_options_alter_users_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['date_joined'], 'verbose_name': 'users'},
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
