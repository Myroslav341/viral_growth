# Generated by Django 3.0.7 on 2020-06-06 14:35

from django.db import migrations, models
import viral_growth_app.library.helpers.models


class Migration(migrations.Migration):

    dependencies = [
        ('viral_growth_app', '0005_auto_20200606_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='viral_growth/default_avatar.png', upload_to=viral_growth_app.library.helpers.models.user_storage_path),
        ),
    ]
