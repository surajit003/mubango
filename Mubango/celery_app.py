import os
from celery import Celery
from Mubango.settings import CELERY_RESULT_BACKEND, CELERY_BROKER_URL, RABBITMQ_VHOST

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mubango.settings")
celery_app = Celery(
    RABBITMQ_VHOST,
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL,
    task_ignore_result=True,
)
celery_app.config_from_object("django.conf:settings")
celery_app.autodiscover_tasks()
