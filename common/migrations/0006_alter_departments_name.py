# Generated by Django 3.2.7 on 2021-10-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20211031_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
