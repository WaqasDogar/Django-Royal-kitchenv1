# Generated by Django 3.2.3 on 2021-06-11 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0026_auto_20210611_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webresources',
            name='Day',
        ),
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 11, 10, 56, 27, 931004)),
        ),
    ]
