# Generated by Django 3.0.3 on 2020-02-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagerevision',
            name='current_interval',
            field=models.SmallIntegerField(default=0),
        ),
    ]
