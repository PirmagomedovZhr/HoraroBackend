# Generated by Django 4.0.5 on 2022-08-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_alter_customuser_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(max_length=15),
        ),
    ]
