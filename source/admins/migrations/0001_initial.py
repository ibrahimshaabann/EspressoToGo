<<<<<<< HEAD
# Generated by Django 4.2.5 on 2023-10-05 16:24
=======
# Generated by Django 4.2.5 on 2023-10-08 07:43
>>>>>>> f7215295e1727762a1d33999583635936d4dfb5a

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminBridge',
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
            name='Admin',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'الادمنز',
                'db_table': 'admins',
            },
            bases=('admins.adminbridge',),
        ),
    ]
