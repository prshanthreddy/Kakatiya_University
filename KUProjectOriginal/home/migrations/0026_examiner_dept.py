# Generated by Django 4.0 on 2022-04-06 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_applications_caste_approved_caste'),
    ]

    operations = [
        migrations.AddField(
            model_name='examiner',
            name='dept',
            field=models.CharField(max_length=200, null=True),
        ),
    ]