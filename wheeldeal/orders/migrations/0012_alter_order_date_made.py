# Generated by Django 3.2.5 on 2021-08-14 00:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_date_made'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_made',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 14, 3, 31, 54, 349044)),
        ),
    ]
