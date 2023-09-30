# Generated by Django 4.2.5 on 2023-09-30 20:32

from django.db import migrations, models
import products.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400, verbose_name='الوصف')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[products.validators.validate_price])),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='وقت الدفع')),
                ('type', models.TextField(choices=[('سلفه', 'Advance Payment'), ('تكلفه', 'Normal Cost')], default='تكلفه')),
            ],
            options={
                'verbose_name': 'Cost',
                'verbose_name_plural': 'Costs',
                'db_table': 'costs',
                'ordering': ['-id'],
            },
        ),
    ]
