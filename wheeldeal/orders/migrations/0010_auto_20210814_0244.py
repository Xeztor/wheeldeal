# Generated by Django 3.2.5 on 2021-08-13 23:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_userprofile_price_for_delivery'),
        ('orders', '0009_auto_20210814_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='profiles.userprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_made',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 14, 2, 44, 24, 753094)),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_guy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_guy', to='profiles.userprofile'),
        ),
    ]
