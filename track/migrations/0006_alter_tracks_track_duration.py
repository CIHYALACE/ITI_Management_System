# Generated by Django 5.1.6 on 2025-03-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0005_alter_tracks_track_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='track_duration',
            field=models.IntegerField(null=True),
        ),
    ]
