# Generated by Django 4.1.3 on 2022-11-12 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="identity",
            name="public_key_id",
            field=models.TextField(blank=True, null=True),
        ),
    ]