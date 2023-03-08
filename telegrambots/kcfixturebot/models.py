from django.db import models


class Schedule(models.Model):
    class Days(models.TextChoices):
        mon = "MON"
        tue = "TUE"
        wed = "WED"
        thu = "THU"
        fri = "FRI"
        sat = "SAT"
        sun = "SUN"

    chat_id = models.IntegerField(unique=True, null=True)
    team_name = models.CharField(max_length=100, null=True)
    channel_username = models.CharField(max_length=30, null=True)
    reminder_day = models.CharField(choices=Days.choices, max_length=30, null=True)
    game_date = models.CharField(max_length=50, null=True)
    game_day = models.CharField(max_length=50, null=True)
    game_time = models.CharField(max_length=50, null=True)
