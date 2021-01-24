from datetime import timedelta
from django.utils import timezone


def get_default_expiration():
    return timezone.now() + timedelta(days=30)
