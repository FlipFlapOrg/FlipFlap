from typing import List, Optional

from pydantic import BaseModel


class UserMangaResponse(BaseModel):
    manga_id: str
    title: str
    author: str
    tags: List[str]
    manga_url: Optional[str] = None
    page_num: int
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


class BookmarkRequest(BaseModel):
    manga_id: str


class HistoryRequest(BaseModel):
    manga_id: str


class TagRequest(BaseModel):
    tags: List[str]


class TagResponse(BaseModel):
    tags: List[str]

class FaveRequest(BaseModel):
    manga_id: str
