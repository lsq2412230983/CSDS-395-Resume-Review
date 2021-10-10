# Generated by Django 3.2 on 2021-10-10 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='finished_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 1, 8, 5, 385554)),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 1, 8, 5, 385528)),
        ),
        migrations.AlterField(
            model_name='order',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]
