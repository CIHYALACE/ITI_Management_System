# Generated by Django 5.1.6 on 2025-03-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='track_date',
            field=models.DateField(null=True),
        ),
    ]
