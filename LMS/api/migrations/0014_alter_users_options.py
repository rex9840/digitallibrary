# Generated by Django 5.0.1 on 2024-01-19 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_users_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['ID'], 'verbose_name': 'users'},
        ),
    ]