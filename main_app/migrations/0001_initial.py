# Generated by Django 4.2.7 on 2024-03-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('species', models.TextField()),
                ('botanical_name', models.TextField()),
                ('notes', models.TextField()),
            ],
        ),
    ]