# Generated by Django 3.2.12 on 2023-12-14 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
