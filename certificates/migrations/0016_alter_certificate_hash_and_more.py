# Generated by Django 4.1.7 on 2023-04-02 13:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0015_alter_certificate_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='hash',
            field=models.TextField(default=uuid.UUID('ea4f6614-dc66-4f2d-881c-d0896d926d22')),
        ),
        migrations.AlterField(
            model_name='certificatevalidation',
            name='status',
            field=models.CharField(blank=True, choices=[('Fake', 'Fake'), ('Clean', 'Clean')], max_length=30, null=True),
        ),
    ]
