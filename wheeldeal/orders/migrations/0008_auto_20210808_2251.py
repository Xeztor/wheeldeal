# Generated by Django 3.2.5 on 2021-08-08 19:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0007_auto_20210808_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_made',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 8, 22, 51, 21, 244678)),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_guy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_guy', to=settings.AUTH_USER_MODEL),
        ),
    ]
