# Generated by Django 4.0.2 on 2023-09-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_driver_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]