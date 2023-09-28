# Generated by Django 4.2.5 on 2023-09-28 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('attendance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='employee_attended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_attendance', to='employees.employee', verbose_name='الموظف'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='user_created_the_attendance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_created', to=settings.AUTH_USER_MODEL, verbose_name='المسئول'),
        ),
    ]
