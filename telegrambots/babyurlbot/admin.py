from django.contrib import admin  # noqa: F401

from telegrambots.babyurlbot.models import UrlMapping

admin.site.register([UrlMapping])
