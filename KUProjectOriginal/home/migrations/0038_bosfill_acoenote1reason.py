# Generated by Django 4.0.3 on 2022-04-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_bosfill_panel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bosfill',
            name='acoeNote1Reason',
            field=models.CharField(default='Accepted', max_length=100, null=True),
        ),
    ]