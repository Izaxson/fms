# Generated by Django 4.2.4 on 2023-09-08 04:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0004_alter_received_date_created_alter_sent_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='received',
            options={'ordering': ['-id'], 'verbose_name': 'Received', 'verbose_name_plural': 'Received'},
        ),
        migrations.AlterField(
            model_name='received',
            name='file',
            field=models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx'])]),
        ),
        migrations.AlterField(
            model_name='sent',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
