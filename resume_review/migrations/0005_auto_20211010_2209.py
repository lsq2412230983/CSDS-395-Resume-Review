# Generated by Django 3.2 on 2021-10-10 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_review', '0004_auto_20211010_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 22, 9, 37, 758523)),
        ),
        migrations.AlterField(
            model_name='order',
            name='finished_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 22, 9, 37, 758539)),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='delivery_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 14, 22, 9, 37, 758068)),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
