# Generated by Django 4.0.5 on 2022-06-15 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_approved_supdept_approved_supwadd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bosfill',
            name='acoeNote1File',
        ),
        migrations.RemoveField(
            model_name='bosfill',
            name='acoeNote2File',
        ),
        migrations.RemoveField(
            model_name='bosfill',
            name='acoeNote3File',
        ),
        migrations.RemoveField(
            model_name='bosfill',
            name='coeNote1File',
        ),
        migrations.RemoveField(
            model_name='bosfill',
            name='coeNote2File',
        ),
        migrations.RemoveField(
            model_name='bosfill',
            name='coeNote3File',
        ),
        migrations.RemoveField(
            model_name='bosfill',
            name='vcNote1File',
        ),
        migrations.RemoveField(
            model_name='bosfill',
            name='vcNote3File',
        ),
    ]