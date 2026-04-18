import os
from datetime import datetime, timezone

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .schemas import ApiStatus

app = FastAPI(title="Wine Starter API", version="1.0.0")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin, "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=ApiStatus)
def root(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return ApiStatus(
        message="Backend FastAPI opérationnel",
        database="connected",
        time=datetime.now(timezone.utc),
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/info")
def api_info():
    return {
        "name": "Wine Starter API",
        "version": "1.0.0",
        "frontend_origin": frontend_origin,
    }