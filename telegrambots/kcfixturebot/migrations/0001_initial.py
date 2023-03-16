# Generated by Django 4.1.3 on 2023-01-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("channel_username", models.CharField(max_length=30)),
                (
                    "fixture_schedule",
                    models.CharField(
                        choices=[
                            ("MONDAY", "Mon"),
                            ("TUESDAY", "Tue"),
                            ("WEDNESDAY", "Wed"),
                            ("THURSDAY", "Thu"),
                            ("FRIDAY", "Fri"),
                            ("SATURDAY", "Sat"),
                            ("SUNDAY", "Sun"),
                        ],
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]