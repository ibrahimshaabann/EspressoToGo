# Generated by Django 4.2.5 on 2023-10-03 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0005_alter_delivery_options_alter_delivery_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='reposnisble_employee',
            new_name='responsible_employee',
        ),
    ]
