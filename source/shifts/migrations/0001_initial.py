# Generated by Django 4.2.5 on 2023-11-01 04:01

from django.db import migrations, models


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
                'verbose_name_plural': 'الشيفتات',
                'db_table': 'shifts',
                'ordering': ['-id'],
            },
        ),
    ]
