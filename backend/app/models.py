from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from .database import Base

class Healthcheck(Base):
    __tablename__ = "healthchecks"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable=False, default="ok")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
