# Generated by Django 4.1 on 2023-01-07 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comment_create_date_comment_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 7, 13, 36, 53, 257821, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 7, 13, 36, 53, 257821, tzinfo=datetime.timezone.utc)),
        ),
    ]
