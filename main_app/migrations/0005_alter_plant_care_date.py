# Generated by Django 4.2.7 on 2024-03-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_plant_care'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant_care',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]
