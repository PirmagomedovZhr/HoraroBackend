# Generated by Django 4.0.5 on 2022-09-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0030_groupusertelegram_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="verified",
            field=models.BooleanField(default=False),
        ),
    ]
