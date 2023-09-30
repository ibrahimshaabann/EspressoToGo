# Generated by Django 4.2.5 on 2023-09-29 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('deliveries', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='reposnisble_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_deliveries', to='employees.employee'),
        ),
    ]
