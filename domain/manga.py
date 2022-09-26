from typing import Optional

from pydantic import BaseModel


class Manga(BaseModel):
    manga_id: str
    title: str
    author: str
    page_num: int
    manga_url: Optional[str] = None
    is_completed: bool = False
