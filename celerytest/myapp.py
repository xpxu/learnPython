# tasks.py
import time
from datetime import timedelta
from celery import Celery

app = Celery('myapp', broker='redis://localhost:6379/0')

# app configuration for celery beat
app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'sendmail-every-3-seconds': {
            'task': 'myapp.sendmail',
            'schedule': timedelta(seconds=0.1),
            'args': [dict(to='xp.xu@python.org')]
        },
    },
    CELERY_TIMEZONE = 'UTC'
)

@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')
