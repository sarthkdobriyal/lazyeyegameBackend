# Generated by Django 4.2.5 on 2023-09-26 23:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_tenant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=25, unique=True, validators=[django.core.validators.RegexValidator(message='Username must consist of 2 to 25 characters and can only contain lowercase letters and digits', regex='^[a-z0-9+]{2,25}$')]),
        ),
    ]
