# Generated by Django 4.0 on 2022-04-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_rename_deptstatus_bosfill_acoestatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bosfill',
            old_name='acoeStatus',
            new_name='acoeNote1Status',
        ),
        migrations.RenameField(
            model_name='bosfill',
            old_name='coeStatus',
            new_name='acoeNote2Status',
        ),
        migrations.RenameField(
            model_name='bosfill',
            old_name='vcStatus',
            new_name='acoeNote3Status',
        ),
        migrations.AddField(
            model_name='bosfill',
            name='coeNote1Status',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bosfill',
            name='coeNote2Status',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bosfill',
            name='coeNote3Status',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bosfill',
            name='vcNote1Status',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bosfill',
            name='vcNote2Status',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bosfill',
            name='vcNote3Status',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
    ]