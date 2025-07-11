# Generated by Django 5.1.6 on 2025-03-17 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0006_alter_tracks_track_duration'),
        ('trainee', '0004_traineeprofile_track_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traineeprofile',
            name='track_id',
        ),
        migrations.AlterField(
            model_name='traineeprofile',
            name='trainee_track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='track.tracks'),
        ),
    ]
