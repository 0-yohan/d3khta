# Generated by Django 4.1.7 on 2023-04-04 16:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dekhta', '0004_post_title_alter_post_d_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='poets',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='d_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 4, 21, 38, 21, 533)),
        ),
    ]
