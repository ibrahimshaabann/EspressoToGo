# Generated by Django 4.2.5 on 2023-10-08 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='responsible_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee'),
        ),
    ]
