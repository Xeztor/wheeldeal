# Generated by Django 3.2.5 on 2021-08-08 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_delivered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_made',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 8, 17, 18, 29, 470797)),
        ),
    ]