from tasks.celery_app import celery_app
from utils.file_utils import delete_session_file

@celery_app.task(name="delete_session_task")
def delete_session_task(session_id: str):
    """Celery task to delete a session file."""
    return delete_session_file(session_id)
