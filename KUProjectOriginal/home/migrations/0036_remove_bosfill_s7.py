# Generated by Django 4.0 on 2022-04-20 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_remove_bosfill_s1_remove_bosfill_s2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bosfill',
            name='s7',
        ),
    ]
