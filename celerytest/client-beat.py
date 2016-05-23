#!/bin/env/python
import os
os.system('celery beat --app myapp --pidfile celery-beat.pidfile')
