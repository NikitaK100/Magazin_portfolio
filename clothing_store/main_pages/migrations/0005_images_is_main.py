# Generated by Django 3.2.12 on 2022-04-11 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0004_auto_20220411_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
