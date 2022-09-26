import datetime
from pydantic import BaseModel


class Bookmark(BaseModel):
    manga_id: str
    user_id: str
    created_at: datetime.datetime
