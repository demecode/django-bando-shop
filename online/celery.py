import os
from celery import Celery

# lets set the default Django settigns for the celery program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online.settings')
app = Celery('online')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()  # look for tasks.py
