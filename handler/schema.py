from typing import List

from pydantic import BaseModel


class MangaResponse(BaseModel):
    manga_id: str
    title: str
    author: str
    image_url: List[str]
    tags: List[str]
    is_faved: bool
    is_bookmarked: bool
