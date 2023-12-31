# Generated by Django 4.2.4 on 2023-08-20 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.URLField(default='https://i.imgur.com/PdQAt6.jpg'),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_edited',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 20, 16, 59, 15, 411858)),
        ),
    ]
