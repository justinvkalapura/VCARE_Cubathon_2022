# Generated by Django 4.0.4 on 2022-05-27 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_age_remove_account_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='district',
            field=models.CharField(choices=[('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Kannur', 'Kannur'), ('Trivandrum', 'Trivandrum'), ('Palakkad', 'Palakkad'), ('Thrissur', 'Thrissur'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Idukki', 'Idukki'), ('Kollam', 'Kollam'), ('Ernakulam', 'Ernakulam'), ('Wayanad', 'Wayanad'), ('Kasaragod', 'Kasaragod'), ('Pathanamthitta', 'Pathanamthitta')], default='Kollam', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 28, 42, 258796)),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='state',
            field=models.CharField(choices=[('kerala', 'kerala'), ('demo', 'demo')], default='Kerala', max_length=50),
            preserve_default=False,
        ),
    ]
