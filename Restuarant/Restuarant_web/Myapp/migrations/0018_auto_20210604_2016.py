# Generated by Django 3.2.3 on 2021-06-04 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0017_alter_customer_entrydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 4, 20, 16, 3, 533978)),
        ),
        migrations.AlterField(
            model_name='food',
            name='FoodImage',
            field=models.ImageField(upload_to='images'),
        ),
    ]
