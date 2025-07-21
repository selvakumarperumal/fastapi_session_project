from middleware.session_middleware import add_session_middleware
from fastapi import FastAPI

app = FastAPI()

add_session_middleware(app)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}