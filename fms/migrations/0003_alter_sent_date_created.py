# Generated by Django 4.2.4 on 2023-09-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0002_remove_received_file_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sent',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
