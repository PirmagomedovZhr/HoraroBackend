# Generated by Django 4.0.5 on 2022-09-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0028_telegramuser_groupusertelegram"),
    ]

    operations = [
        migrations.AlterField(
            model_name="telegramuser",
            name="telegram_id",
            field=models.TextField(unique=True),
        ),
    ]
