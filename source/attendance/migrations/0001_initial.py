<<<<<<< HEAD
# Generated by Django 4.2.5 on 2023-10-05 16:24
=======
# Generated by Django 4.2.5 on 2023-10-08 07:43
>>>>>>> f7215295e1727762a1d33999583635936d4dfb5a

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت الدخول')),
                ('out_time', models.DateTimeField(blank=True, null=True, verbose_name='وقت الخروج')),
            ],
            options={
                'verbose_name_plural': 'الحضور والانصراف',
                'db_table': 'Attendance',
                'ordering': ['-in_time'],
            },
        ),
    ]
