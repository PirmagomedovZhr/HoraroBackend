# Generated by Django 4.0.5 on 2022-08-20 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0017_alter_customuser_group_alter_faculty_name_and_more"),
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
