# Generated by Django 4.0.2 on 2023-08-26 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nextacloudapp', '0004_remove_store_manager_staff_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='brand',
            new_name='brand_name',
        ),
    ]
