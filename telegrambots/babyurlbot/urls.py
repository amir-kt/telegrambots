from django.urls import path

from .views import bot_webhook, heartbeat, poll_bot_updates, redirect

urlpatterns = [
    path("heartbeat/", heartbeat, name="heartbeat"),
    path("webhook/<str:token>/", bot_webhook, name="webhook"),
    path("poll/<str:token>/", poll_bot_updates, name="polling"),
    path("redirect/<str:uuid>", redirect, name="redirect"),
]
