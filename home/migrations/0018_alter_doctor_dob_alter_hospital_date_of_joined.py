# Generated by Django 4.0.4 on 2022-06-02 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_doctor_dob_alter_hospital_date_of_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 23, 9, 26, 320335)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='date_of_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 23, 9, 26, 319335)),
        ),
    ]
