# Generated by Django 4.0.5 on 2023-02-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0043_alter_telegramuser_notification_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="telegramuser",
            name="username",
            field=models.TextField(default="Username doesn't exists"),
        ),
    ]
