# Generated by Django 3.2.8 on 2021-10-20 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_review', '0014_auto_20211020_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='finished_at',
            field=models.DateTimeField(null=True),
        ),
    ]
