# Generated by Django 4.0.2 on 2022-07-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_applications_sem1_applications_sem2_approved_sem1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='plagairismStatus',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
    ]
