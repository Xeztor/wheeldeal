# Generated by Django 3.2.5 on 2021-08-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='price_for_delivery',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
