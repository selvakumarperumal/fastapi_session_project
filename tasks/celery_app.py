from celery import Celery

celery_app = Celery("session_tasks",
                   broker="redis://redis_container:6379/0")
