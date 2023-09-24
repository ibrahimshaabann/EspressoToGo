# Generated by Django 4.2.5 on 2023-09-24 20:10

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(db_index=True, max_length=20, unique=True, validators=[users.validators.valid_phone_number]),
        ),
    ]
