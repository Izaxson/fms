# Generated by Django 4.2.4 on 2023-09-11 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0006_alter_received_options_alter_sent_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='received',
            name='county',
            field=models.CharField(blank=True, choices=[('Mandera_County', 'Mandera County'), ('Wajir_County', 'Wajir County'), ('Garissa_County', 'Garissa County')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='received',
            name='entity',
            field=models.CharField(choices=[('National', 'National'), ('County', 'County'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='received',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=100),
        ),
    ]
