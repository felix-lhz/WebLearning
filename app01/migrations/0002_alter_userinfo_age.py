# Generated by Django 5.1.1 on 2024-10-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
