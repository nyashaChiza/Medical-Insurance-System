# Generated by Django 3.2 on 2023-03-06 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service_providers', '0003_rename_created_at_serviceprovider_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patience_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('gender', models.URLField(choices=[('M', 'Male'), ('F', 'Female')], max_length=255)),
                ('date_of_birth', models.DateTimeField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cause', models.CharField(max_length=255)),
                ('employer', models.CharField(max_length=255)),
                ('patient_suffix', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=255)),
                ('number_of_dependants', models.CharField(max_length=255)),
                ('fee_charged', models.CharField(max_length=255)),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='service_providers.serviceprovider')),
            ],
        ),
    ]
