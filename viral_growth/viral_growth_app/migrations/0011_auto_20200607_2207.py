# Generated by Django 3.0.7 on 2020-06-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viral_growth_app', '0010_auto_20200607_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='page',
            name='profile_info',
        ),
        migrations.AddField(
            model_name='page',
            name='bio',
            field=models.TextField(default='Profile info'),
        ),
    ]
