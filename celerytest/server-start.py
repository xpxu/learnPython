import os
os.system('celery -A myapp  worker -c 1 --loglevel=info --pidfile celery-worker.pidfile') 
