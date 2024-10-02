# Generated by Django 5.1.1 on 2024-10-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "EmployeeManagementSystem",
            "0004_prettynum_rename_user_account_userinfo_account_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="prettynum",
            name="level",
            field=models.SmallIntegerField(
                choices=[(0, "Normal"), (1, "VIP1"), (2, "VIP2"), (3, "VIP3")],
                default=0,
                verbose_name="Level",
            ),
        ),
    ]
