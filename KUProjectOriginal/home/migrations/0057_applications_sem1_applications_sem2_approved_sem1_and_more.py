# Generated by Django 4.0.3 on 2022-07-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_applications_prephdmonthandyear_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='sem1',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='applications',
            name='sem2',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='approved',
            name='sem1',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='approved',
            name='sem2',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]