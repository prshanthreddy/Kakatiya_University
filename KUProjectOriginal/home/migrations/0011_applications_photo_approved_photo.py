# Generated by Django 4.0 on 2022-01-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_applications_titlethesis_approved_titlethesis'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='approved',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
