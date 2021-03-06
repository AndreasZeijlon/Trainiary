# Generated by Django 3.1.7 on 2021-05-15 23:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainiary_app', '0008_auto_20210516_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myevent',
            name='distance',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='myevent',
            name='duration',
            field=models.TimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='myevent',
            name='intensity',
            field=models.IntegerField(default=0),
        ),
    ]
