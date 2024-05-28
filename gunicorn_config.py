bind = "0.0.0.0:8000"
# Nombre de workers, ajustez en fonction des ressources de votre serveur
workers = 4  
worker_class = "uvicorn.workers.UvicornWorker"
loglevel = "info"
accesslog = "/home/aniang/OptiDrive/access.log"
errorlog = "/home/aniang/OptiDrive/logs/error.log"
#loglevel = "info"
#accesslog = "/var/log/gunicorn/access.log"
#errorlog = "/var/log/gunicorn/error.log"
