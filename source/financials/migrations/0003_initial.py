# Generated by Django 4.2.5 on 2023-09-29 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('financials', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee', verbose_name='مسئول الشيفت'),
        ),
    ]
