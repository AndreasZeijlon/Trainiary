# Generated by Django 3.1.7 on 2021-04-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainiary_app', '0002_workout_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]