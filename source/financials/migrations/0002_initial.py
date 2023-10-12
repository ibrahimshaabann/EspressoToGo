# Generated by Django 4.2.5 on 2023-10-12 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('financials', '0001_initial'),
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost',
            name='related_shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shifts.shift', verbose_name='الشيفت المرتبط'),
        ),
    ]
