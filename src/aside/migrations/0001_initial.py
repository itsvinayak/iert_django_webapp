# Generated by Django 2.1.5 on 2019-02-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="faculty",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("Designation", models.CharField(max_length=400)),
                ("Qualification", models.CharField(max_length=500)),
                ("phone", models.CharField(max_length=12)),
                ("email", models.EmailField(max_length=254)),
            ],
        )
    ]
