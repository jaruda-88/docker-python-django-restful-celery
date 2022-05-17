import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jaruda_back.settings')

app = Celery('jaruda_back')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule = {
#     'every-15-second': {
#         'task': 'todos.tasks.say_hello',
#         'schedule': 15,
#         'args': (,)
#     }
# }

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))