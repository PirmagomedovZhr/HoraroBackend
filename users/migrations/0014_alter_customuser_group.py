# Generated by Django 4.0.5 on 2022-08-18 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_alter_customuser_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="group",
            field=models.OneToOneField(
                error_messages={
                    "unique": "Группа с таким именем уже зарегистрирована."
                },
                on_delete=django.db.models.deletion.CASCADE,
                to="users.group",
            ),
        ),
    ]