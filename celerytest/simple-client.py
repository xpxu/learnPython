from myapp import sendmail

sendmail.delay(dict(to='celery@python.org'))
