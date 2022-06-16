import json
from celery import Celery
from app.core.config import settings


app = Celery("worker")
app.config_from_object(json.loads(settings.json()), namespace="API_CELERY")
app.autodiscover_tasks(["app"])
shared_task = app.task
