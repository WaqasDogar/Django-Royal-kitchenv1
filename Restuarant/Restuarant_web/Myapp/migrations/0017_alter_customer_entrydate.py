# Generated by Django 3.2.3 on 2021-06-04 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0016_alter_customer_entrydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 4, 19, 32, 49, 974069)),
        ),
    ]
