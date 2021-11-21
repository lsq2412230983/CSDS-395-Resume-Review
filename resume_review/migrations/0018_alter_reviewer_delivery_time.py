# Generated by Django 3.2.8 on 2021-10-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_review', '0017_auto_20211031_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='delivery_time',
            field=models.CharField(choices=[('delivery_1', 'One week'), ('delivery_2', 'Two weeks'), ('delivery_3', 'Three weeks'), ('delivery_4', 'Four weeks or more')], default='delivery_1', max_length=255),
        ),
    ]