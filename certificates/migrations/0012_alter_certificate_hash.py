# Generated by Django 4.1.7 on 2023-03-11 09:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("certificates", "0011_alter_certificate_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="hash",
            field=models.TextField(
                default=uuid.UUID("1d315c0a-46a6-45ca-a17c-51e0a4b291f1")
            ),
        ),
    ]