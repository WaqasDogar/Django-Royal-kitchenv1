# Generated by Django 3.2.3 on 2021-06-11 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0023_auto_20210611_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='webresources',
            name='Day',
            field=models.CharField(default='Monday', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 11, 10, 53, 5, 255579)),
        ),
    ]