# Generated by Django 2.1.5 on 2019-03-02 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("iert_news", "0015_comment")]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]
