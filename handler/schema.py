from typing import List, Optional

from pydantic import BaseModel


class UserMangaResponse(BaseModel):
    manga_id: str
    title: str
    author: str
    tags: List[str]
    manga_url: Optional[str] = None
    is_faved: bool
    is_bookmarked: bool


class MangaRequest(BaseModel):
    title: str
    author: str
    tags: List[str]
    page_num: int
    manga_url: Optional[str] = None


class MangaResponse(BaseModel):
    manga_id: str
    title: str
    author: str
    tags: List[str]
    manga_url: Optional[str] = None
    page_num: int


class HistoryRequest(BaseModel):
    manga_id: str
