# Generated by Django 4.2.5 on 2023-09-30 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='وقت البداية')),
                ('end_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='وقت النهاية')),
            ],
            options={
                'verbose_name': 'Shift',
                'verbose_name_plural': 'shifts',
                'db_table': 'shifts',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ShiftReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_profit', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='اجمالي الربح')),
                ('total_costs', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='اجمالي التكلفة')),
                ('net_profit', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='صافي الربح')),
                ('related_shift', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='shifts', to='shifts.shift', verbose_name='الشيفت')),
            ],
            options={
                'verbose_name': 'Shift Report',
                'verbose_name_plural': 'Shifts Reports',
                'db_table': 'shifts_reports',
                'ordering': ['-id'],
            },
        ),
    ]
