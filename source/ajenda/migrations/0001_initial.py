# Generated by Django 4.2.5 on 2023-11-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(verbose_name='ملاحظه')),
            ],
            options={
                'verbose_name': 'ملحوظة',
                'verbose_name_plural': 'ملاحظات',
                'db_table': 'ajenda',
            },
        ),
    ]
