# Generated by Django 4.1.3 on 2022-12-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manga", "0006_remove_genre_self_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="manga",
            name="dir",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
