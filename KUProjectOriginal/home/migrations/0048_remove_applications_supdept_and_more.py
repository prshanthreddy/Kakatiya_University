# Generated by Django 4.0 on 2022-06-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_alter_bosfill_vcnote1date_alter_bosfill_vcnote2date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='supdept',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='supwadd',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='yearofadd',
        ),
        migrations.RemoveField(
            model_name='approved',
            name='supdept',
        ),
        migrations.RemoveField(
            model_name='approved',
            name='supwadd',
        ),
        migrations.RemoveField(
            model_name='approved',
            name='yearofadd',
        ),
        migrations.AddField(
            model_name='bosfill',
            name='vcNote1File',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='bosfill',
            name='vcNote2File',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='bosfill',
            name='vcNote3File',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='applications',
            name='article',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='applications',
            name='prephd',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='approved',
            name='article',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='approved',
            name='prephd',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
