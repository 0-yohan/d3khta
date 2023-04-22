# Generated by Django 4.1.7 on 2023-04-21 02:31

import datetime
import dekhta.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dekhta', '0012_alter_post_d_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='poets',
            name='pfp',
            field=models.ImageField(default='default.jpg', upload_to=dekhta.models.PoetProfilePicPath('pfps')),
        ),
        migrations.AlterField(
            model_name='post',
            name='d_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 8, 1, 9, 282338)),
        ),
    ]