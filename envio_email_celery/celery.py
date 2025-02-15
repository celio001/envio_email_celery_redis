import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'envio_email_celery.settings')

app = Celery('envio_email_celery')

app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')