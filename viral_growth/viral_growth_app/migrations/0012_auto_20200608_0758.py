# Generated by Django 3.0.7 on 2020-06-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viral_growth_app', '0011_auto_20200607_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='page',
            name='bio',
            field=models.TextField(default='Profile bio'),
        ),
    ]