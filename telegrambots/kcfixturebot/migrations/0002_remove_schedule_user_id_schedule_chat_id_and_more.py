# Generated by Django 4.1.3 on 2023-01-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kcfixturebot", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schedule",
            name="user_id",
        ),
        migrations.AddField(
            model_name="schedule",
            name="chat_id",
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="channel_username",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="fixture_schedule",
            field=models.CharField(
                choices=[
                    ("MON", "Mon"),
                    ("TUE", "Tue"),
                    ("WED", "Wed"),
                    ("THU", "Thu"),
                    ("FRI", "Fri"),
                    ("SAT", "Sat"),
                    ("SUN", "Sun"),
                ],
                max_length=30,
                null=True,
            ),
        ),
    ]