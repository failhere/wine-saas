import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL.replace("postgres://", "postgresql+psycopg://"),
    pool_pre_ping=True
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
