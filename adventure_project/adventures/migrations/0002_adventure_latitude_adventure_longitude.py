# Generated by Django 4.2.2 on 2023-06-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adventures", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="adventure",
            name="latitude",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="adventure",
            name="longitude",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
