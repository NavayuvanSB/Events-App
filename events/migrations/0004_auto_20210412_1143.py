# Generated by Django 3.2 on 2021-04-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210412_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtime',
            name='event_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='eventtime',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='end time of the event'),
        ),
        migrations.AlterField(
            model_name='eventtime',
            name='from_time',
            field=models.TimeField(blank=True, null=True, verbose_name='start time of the event'),
        ),
    ]
