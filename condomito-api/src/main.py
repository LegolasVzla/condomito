
from io import BytesIO

from fastapi import (
    Depends,
    FastAPI,
    Response,
    Request
)



app = FastAPI(
    title='condomito api',
    description='app for management of condominium',
    version='0.1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/healthz")
async def healthz(
) -> None:
    return {"health": "ok"}