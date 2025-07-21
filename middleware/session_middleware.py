from fastapi import Request, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
import uuid
from utils.file_utils import create_session_file
from tasks.session_tasks import delete_session_task

class SessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        session_id = request.cookies.get("session_id")
        response = await call_next(request)
        print(f"Session ID from cookies: {session_id}")
        if not session_id:
            print("No session ID found, creating a new one.")
            session_id = str(uuid.uuid4())
            response.set_cookie(key="session_id",
                                value=session_id,
                                expires=60,
                                httponly=True,
                                samesite="lax")
            
            create_session_file(session_id)
            delete_session_task.apply_async((session_id,), countdown=60)
        return response
        
def add_session_middleware(app: FastAPI):
    app.add_middleware(SessionMiddleware)