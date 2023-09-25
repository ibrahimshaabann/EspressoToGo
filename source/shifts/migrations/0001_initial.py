# Generated by Django 4.2.5 on 2023-09-24 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='وقت البداية')),
                ('end_time', models.DateTimeField(auto_now=True, null=True, verbose_name='وقت النهايه')),
                ('responsible_employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.employee')),
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
                ('total_profit', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='اجمالي الربح')),
                ('total_costs', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='')),
                ('net_profit', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='صافي الربح')),
                ('related_shift', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='shifts.shift', verbose_name='الشيفت')),
            ],
            options={
                'verbose_name': 'Shift Reprt',
                'verbose_name_plural': 'shifts_reports',
                'db_table': 'shifts_reports',
                'ordering': ['-id'],
            },
        ),
    ]
