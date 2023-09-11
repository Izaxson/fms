# Generated by Django 4.2.4 on 2023-09-11 03:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0005_alter_received_options_alter_received_file_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='received',
            options={'ordering': ['-date_received'], 'verbose_name': 'Received', 'verbose_name_plural': 'Received'},
        ),
        migrations.AlterModelOptions(
            name='sent',
            options={'ordering': ['-date_sent'], 'verbose_name': 'Sent', 'verbose_name_plural': 'Sent'},
        ),
        migrations.AlterField(
            model_name='received',
            name='file',
            field=models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='sent',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sent',
            name='file',
            field=models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]