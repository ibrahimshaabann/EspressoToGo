# Generated by Django 4.2.5 on 2023-10-18 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import employees.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeBridge',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employee_role', models.CharField(choices=[('OWNER', 'Owner'), ('MANAGER', 'Manager'), ('CASHIER', 'Cashier'), ('CHEF', 'Chef'), ('WAITER', 'Waiter'), ('CLEANER', 'Cleaner')], max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, validators=[employees.validators.valid_salary])),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'الموظفين',
                'db_table': 'employees',
            },
            bases=('employees.employeebridge',),
        ),
    ]
