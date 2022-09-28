import datetime
from pydantic import BaseModel

class History(BaseModel):
    manga_id: str
    user_id: str
    page_ratio: float
    created_at: datetime.datetime
