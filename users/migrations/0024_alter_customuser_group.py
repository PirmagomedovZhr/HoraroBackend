# Generated by Django 4.0.5 on 2022-08-20 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0023_alter_customuser_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="group",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="users.group"
            ),
        ),
    ]
