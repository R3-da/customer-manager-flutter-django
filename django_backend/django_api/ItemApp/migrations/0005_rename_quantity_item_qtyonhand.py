# Generated by Django 5.0 on 2023-12-29 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ItemApp', '0004_rename_qtyonhand_item_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='quantity',
            new_name='qtyOnHand',
        ),
    ]