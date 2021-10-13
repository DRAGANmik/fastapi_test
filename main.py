import uvicorn
from fastapi import FastAPI, Request, Response

from core.database import SessionLocal
from routes import routes

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    """
    Open db session for every request
    after use closes it
    """
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response


app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
