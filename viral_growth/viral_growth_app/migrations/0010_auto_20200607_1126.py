# Generated by Django 3.0.7 on 2020-06-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viral_growth_app', '0009_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.ImageField(upload_to=''),
        ),
    ]