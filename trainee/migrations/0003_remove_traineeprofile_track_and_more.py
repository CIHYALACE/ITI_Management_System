# Generated by Django 5.1.6 on 2025-03-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_traineeprofile_trainee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='traineeprofile',
            name='trainee_track',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
