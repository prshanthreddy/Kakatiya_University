# Generated by Django 4.0.3 on 2022-04-26 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_remove_bosfill_s7'),
    ]

    operations = [
        migrations.AddField(
            model_name='bosfill',
            name='panel',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
