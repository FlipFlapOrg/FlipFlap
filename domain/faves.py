import datetime
from pydantic import BaseModel


class Faves(BaseModel):
    user_id: str
    manga_id: str
    created_at: datetime.datetime
