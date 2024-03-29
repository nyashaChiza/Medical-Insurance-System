# Generated by Django 4.1.7 on 2023-03-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("claims", "0004_remove_claim_number_of_dependants_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="claim",
            name="relationship",
            field=models.CharField(
                choices=[
                    (1, "Single"),
                    (2, "Husband"),
                    (3, "Wife"),
                    (4, "Brother"),
                    (5, "Sister"),
                    (6, "Aunt"),
                    (7, "Grandmother"),
                    (8, "Uncle"),
                    (9, "Grandfather"),
                    (10, "Nephew"),
                    (11, "Niece"),
                    (12, "Other"),
                ],
                max_length=255,
            ),
        ),
    ]
