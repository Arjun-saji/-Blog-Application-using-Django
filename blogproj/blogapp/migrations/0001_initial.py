# Generated by Django 5.1.1 on 2024-09-04 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600)),
                ('description', models.TextField()),
                ('created_by', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 9, 4, 11, 53, 9, 315280, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
