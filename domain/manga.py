import datetime

from pydantic import BaseModel


class Manga(BaseModel):
    manga_id: str
    title: str
    author: str
    page_num: int
    is_completed: bool = False
    created_at: datetime.datetime
