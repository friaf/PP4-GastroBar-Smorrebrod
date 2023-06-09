# Generated by Django 3.2.18 on 2023-05-03 17:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=False, max_digits=4)),
                ('image', cloudinary.models.CloudinaryField(default=False, max_length=255, verbose_name='image')),
            ],
        ),
    ]
