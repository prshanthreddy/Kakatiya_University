# Generated by Django 4.0.5 on 2022-06-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_applications_supdept_applications_supwadd'),
    ]

    operations = [
        migrations.AddField(
            model_name='approved',
            name='supdept',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='approved',
            name='supwadd',
            field=models.CharField(max_length=200, null=True),
        ),
    ]