# Generated by Django 4.0 on 2022-01-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_applications_mydate_alter_approved_mydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='pc',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='approved',
            name='pc',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
