# Generated by Django 4.0.2 on 2023-08-26 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nextacloudapp', '0007_rename_brand_name_items_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='item',
            new_name='item_name',
        ),
        migrations.RemoveField(
            model_name='items',
            name='type_item',
        ),
    ]
