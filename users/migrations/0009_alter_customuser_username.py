# Generated by Django 4.0.5 on 2022-08-16 09:04

from django.db import migrations, models

import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_alter_customuser_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "Логин занят."},
                max_length=15,
                unique=True,
                validators=[users.validators.UnicodeUsernameValidator()],
            ),
        ),
    ]
