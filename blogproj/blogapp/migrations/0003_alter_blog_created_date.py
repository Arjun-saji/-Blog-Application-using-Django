# Generated by Django 5.1.1 on 2024-09-04 12:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_image_alter_blog_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
