import os
os.system('celery -A myapp  worker --loglevel=info --pidfile celery-worker.pidfile') 
