# Generated by Django 4.2.5 on 2023-10-05 16:24

import django.contrib.auth.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('CUSTOMER', 'Customer'), ('EMPLOYEE', 'Employee')], max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='password')),
                ('is_superuser', models.BooleanField(blank=True, default=False, null=True)),
                ('phone_number', models.CharField(db_index=True, max_length=20, null=True, unique=True, validators=[users.validators.valid_phone_number])),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
