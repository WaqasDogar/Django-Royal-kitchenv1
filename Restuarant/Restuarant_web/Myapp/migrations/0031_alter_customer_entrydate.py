# Generated by Django 3.2.3 on 2021-06-11 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0030_auto_20210611_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 11, 11, 28, 26, 260354)),
        ),
    ]
