# Generated by Django 4.1.7 on 2023-03-10 21:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("certificates", "0007_alter_certificatevalidation_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="hash",
            field=models.TextField(default=uuid.uuid4),
        ),
    ]
