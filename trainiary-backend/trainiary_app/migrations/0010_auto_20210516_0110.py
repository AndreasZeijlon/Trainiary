# Generated by Django 3.1.7 on 2021-05-15 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainiary_app', '0009_auto_20210516_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myevent',
            name='duration',
            field=models.CharField(max_length=200),
        ),
    ]