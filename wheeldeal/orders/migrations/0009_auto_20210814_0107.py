# Generated by Django 3.2.5 on 2021-08-13 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210808_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_made',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 14, 1, 7, 52, 969028)),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('Small Package', 'Small Package'), ('Small Box', 'Small Box'), ('Medium Box', 'Medium Box'), ('Large Box', 'Large Box')], max_length=30),
        ),
    ]
