# Generated by Django 4.2.5 on 2023-10-26 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('shifts', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='customers.customer', verbose_name='العميل'),
        ),
        migrations.AddField(
            model_name='order',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shifts.shift', verbose_name='الشيفت'),
        ),
    ]
