# Generated by Django 3.1.7 on 2021-04-25 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainiary_app', '0005_auto_20210425_1203'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Workout',
            new_name='MyEvent',
        ),
    ]