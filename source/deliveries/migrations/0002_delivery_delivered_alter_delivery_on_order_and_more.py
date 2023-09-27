# Generated by Django 4.2.5 on 2023-09-26 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
        ('employees', '0001_initial'),
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='on_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_deliveries', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='reposnisble_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_deliveries', to='employees.employee'),
        ),
    ]
