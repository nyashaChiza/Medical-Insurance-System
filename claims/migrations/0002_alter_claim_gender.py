# Generated by Django 3.2 on 2023-03-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=255),
        ),
    ]
