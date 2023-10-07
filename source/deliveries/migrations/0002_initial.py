# Generated by Django 4.2.5 on 2023-10-05 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0002_initial'),
        ('employees', '0001_initial'),
        ('deliveries', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_delivery', to='customers.customer'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='for_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_deliveries', to='orders.order'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='responsible_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_deliveries', to='employees.employee'),
        ),
    ]
