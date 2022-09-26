from typing import List

from pydantic import BaseModel


class UserMangaResponse(BaseModel):
    manga_id: str
    title: str
    author: str
    image_url: List[str]
    tags: List[str]
    is_faved: bool
    is_bookmarked: bool


class MangaRequest(BaseModel):
    title: str
    author: str
    tags: List[str]
    page_num: int


class MangaResponse(BaseModel):
    manga_id: str
    title: str
    author: str
    tags: List[str]
    page_num: int
