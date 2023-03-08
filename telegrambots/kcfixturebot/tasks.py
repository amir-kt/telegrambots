from config import celery_app

from .models import Schedule


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return Schedule.objects.count()
