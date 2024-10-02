# Generated by Django 5.1.1 on 2024-10-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EmployeeManagementSystem", "0003_alter_userinfo_user_gender"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrettyNum",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mobile",
                    models.CharField(max_length=11, verbose_name="Phone number"),
                ),
                (
                    "price",
                    models.IntegerField(blank=True, null=True, verbose_name="Price"),
                ),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(0, "Normal"), (1, "VIP1"), (3, "VIP3"), (2, "VIP2")],
                        default=0,
                        verbose_name="Level",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(0, "Normal"), (1, "Disabled")],
                        default=0,
                        verbose_name="Status",
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="userinfo",
            old_name="user_account",
            new_name="account",
        ),
        migrations.RenameField(
            model_name="userinfo",
            old_name="user_age",
            new_name="age",
        ),
        migrations.RenameField(
            model_name="userinfo",
            old_name="user_create_time",
            new_name="create_time",
        ),
        migrations.RenameField(
            model_name="userinfo",
            old_name="user_gender",
            new_name="gender",
        ),
        migrations.RenameField(
            model_name="userinfo",
            old_name="user_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="userinfo",
            old_name="user_password",
            new_name="password",
        ),
    ]
