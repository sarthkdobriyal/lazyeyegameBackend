# Generated by Django 4.2.4 on 2023-09-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacmandata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rollexdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tetrisdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
