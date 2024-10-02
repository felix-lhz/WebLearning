# Generated by Django 5.1.1 on 2024-10-02 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                    "department_name",
                    models.CharField(max_length=100, verbose_name="Department"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
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
                ("user_name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "user_password",
                    models.CharField(max_length=100, verbose_name="Password"),
                ),
                ("user_age", models.IntegerField(verbose_name="Age")),
                (
                    "user_account",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Account balance",
                    ),
                ),
                ("user_create_time", models.DateTimeField(verbose_name="Entry Time")),
                (
                    "user_gender",
                    models.SmallIntegerField(
                        choices=[(2, "female"), (1, "male")], verbose_name="gender"
                    ),
                ),
                (
                    "depart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmployeeManagementSystem.department",
                    ),
                ),
            ],
        ),
    ]
