# Generated by Django 4.1.7 on 2023-03-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('affoz_code', models.CharField(max_length=255, unique=True)),
                ('website', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('contact_personal_email', models.EmailField(max_length=254, unique=True)),
                ('certificate', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
