# Generated by Django 5.0.7 on 2024-07-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetup",
            name="image",
            field=models.ImageField(default="test", upload_to="images"),
            preserve_default=False,
        ),
    ]