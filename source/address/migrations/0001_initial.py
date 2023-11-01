# Generated by Django 4.2.5 on 2023-11-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='العنوان')),
            ],
            options={
                'verbose_name_plural': 'العناوين',
                'db_table': 'address',
            },
        ),
    ]
