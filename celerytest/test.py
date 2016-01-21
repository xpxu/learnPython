from tasks import sendmail

sendmail.delay(dict(to='celery@python.org'))
