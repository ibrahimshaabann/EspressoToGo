# Generated by Django 4.2.5 on 2023-09-25 18:20

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_person_full_name_alter_person_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, null=True, unique=True, validators=[users.validators.is_valid_email]),
        ),
    ]
