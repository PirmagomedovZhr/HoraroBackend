# Generated by Django 4.0.5 on 2022-08-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0008_blockuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="moderator",
            field=models.TextField(default=False),
        ),
    ]
