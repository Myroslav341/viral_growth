# Generated by Django 3.0.7 on 2020-06-06 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viral_growth_app', '0007_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='page',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='viral_growth_app.Page'),
        ),
    ]
