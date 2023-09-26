# Generated by Django 4.2.5 on 2023-09-26 22:51

from django.db import migrations, models
import django.db.models.deletion
import products.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=95, verbose_name='category name')),
            ],
            options={
                'verbose_name': 'Catrgory',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, validators=[products.validators.validate_price], verbose_name='price')),
                ('available', models.BooleanField(default=True, verbose_name='is_available')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'menu_items',
                'db_table': 'menu_items',
                'ordering': ['-id'],
            },
        ),
    ]
