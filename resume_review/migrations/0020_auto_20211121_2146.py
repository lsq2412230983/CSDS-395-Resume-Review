# Generated by Django 3.2.8 on 2021-11-21 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_review', '0019_auto_20211121_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.account'),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.account'),
        ),
        migrations.AlterField(
            model_name='room',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume_review.reviewer'),
        ),
    ]
