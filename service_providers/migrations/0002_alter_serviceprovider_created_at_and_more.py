# Generated by Django 4.1.7 on 2023-03-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_providers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
