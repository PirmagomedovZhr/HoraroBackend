# Generated by Django 4.0.5 on 2022-07-04 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0004_userprofile_block"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="block",
        ),
    ]