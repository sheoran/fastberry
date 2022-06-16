# This will make sure the celery and settings are always initialized
from .celery_app import app as celery_app

__all__ = ("celery_app",)
