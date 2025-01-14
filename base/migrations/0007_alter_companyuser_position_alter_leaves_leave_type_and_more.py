# Generated by Django 5.1.4 on 2025-01-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_alter_companyuser_position_alter_leaves_leave_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyuser",
            name="position",
            field=models.CharField(
                choices=[("employee", "employee"), ("manager", "manager")],
                default="employee",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="leaves",
            name="leave_type",
            field=models.CharField(
                choices=[("casual", "casual"), ("sick", "sick")],
                default="casual",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="leaves",
            name="status",
            field=models.CharField(
                choices=[("casual", "casual"), ("sick", "sick")],
                default="pending",
                max_length=100,
            ),
        ),
    ]
