# Generated by Django 4.0.5 on 2022-09-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0031_customuser_verified"),
    ]

    operations = [
        migrations.AddField(
            model_name="telegramuser",
            name="is_moder",
            field=models.BooleanField(default=False),
        ),
    ]
