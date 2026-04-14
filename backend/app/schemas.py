from datetime import datetime
from pydantic import BaseModel

class ApiStatus(BaseModel):
    message: str
    database: str
    time: datetime
