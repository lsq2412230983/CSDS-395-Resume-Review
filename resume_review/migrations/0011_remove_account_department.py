# Generated by Django 3.2 on 2021-10-14 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_review', '0010_account_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='department',
        ),
    ]
