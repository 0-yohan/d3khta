# Generated by Django 4.1.7 on 2023-04-18 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dekhta', '0010_alter_post_d_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='d_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 3, 58, 6, 472621)),
        ),
    ]
