# Generated by Django 4.0.4 on 2022-05-27 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='date_of_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 23, 25, 12, 36962)),
        ),
    ]