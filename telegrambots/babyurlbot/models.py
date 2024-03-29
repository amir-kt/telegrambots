from django.db import models


class TelegramChat(models.Model):
    """
    Represents a `chat` type from Bot API:
        https://core.telegram.org/bots/api#chat
    """

    class ChatTypes(models.TextChoices):
        PRIVATE = (
            "private",
            "private",
        )
        GROUP = (
            "group",
            "group",
        )
        SUPER_GROUP = (
            "supergroup",
            "supergroup",
        )
        CHANNEL = "channel", "channel"

    telegram_id = models.CharField(max_length=128, unique=True)
    type = models.CharField(choices=ChatTypes.choices, max_length=16)
    title = models.CharField(max_length=512, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)

    def is_private(self):
        return self.type == self.ChatTypes.PRIVATE

    def __str__(self):
        return f"{self.title} ({self.telegram_id})"


class TelegramUser(models.Model):
    """
    Represented a `user` type from Bot API:
        https://core.telegram.org/bots/api#user
    """

    telegram_id = models.CharField(max_length=128, unique=True)
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (@{self.username})"


class UrlMapping(models.Model):
    """
    Represents a mapping from a baby url to a long url
    """

    baby_url = models.URLField(primary_key=True)
    target_url = models.URLField(max_length=1000)

    def __str__(self):
        return f"{self.baby_url} -> {self.target_url}"
