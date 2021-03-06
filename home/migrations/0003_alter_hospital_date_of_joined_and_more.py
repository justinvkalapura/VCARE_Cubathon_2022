# Generated by Django 4.0.4 on 2022-05-27 04:31

import ckeditor.fields
import cloudinary.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_hospital_date_of_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='date_of_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 10, 1, 35, 33920)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='district',
            field=models.CharField(choices=[('Kottayam', 'Kottayam')], max_length=50),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('contact', models.BigIntegerField()),
                ('d_image', cloudinary.models.CloudinaryField(blank=True, max_length=255)),
                ('yos', models.IntegerField()),
                ('dob', models.DateTimeField(default=datetime.datetime(2022, 5, 27, 10, 1, 35, 33920))),
                ('fee', models.IntegerField()),
                ('sex', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('qualification', ckeditor.fields.RichTextField()),
                ('h_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.hospital')),
                ('s_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.specialization')),
            ],
        ),
    ]
