# Generated by Django 4.1 on 2023-01-06 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 9, 46, 55, 848733, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 9, 46, 55, 848733, tzinfo=datetime.timezone.utc)),
        ),
    ]
