# Generated by Django 4.0.1 on 2022-02-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
