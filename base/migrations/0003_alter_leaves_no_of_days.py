# Generated by Django 5.1.4 on 2025-01-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_companyuser_position_leaves"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaves",
            name="no_of_days",
            field=models.IntegerField(default=0),
        ),
    ]