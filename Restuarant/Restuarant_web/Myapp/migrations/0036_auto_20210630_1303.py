# Generated by Django 3.2.4 on 2021-06-30 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0035_auto_20210630_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 30, 13, 3, 56, 923289)),
        ),
        migrations.AlterField(
            model_name='ordereproduct',
            name='CustomerID',
            field=models.IntegerField(null=True),
        ),
    ]
