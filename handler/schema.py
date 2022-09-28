from typing import List

from pydantic import BaseModel


class ServiceUrl(BaseModel):
    service_name: str
    url: str


class UserMangaResponse(BaseModel):
    manga_id: str
    title: str
    author: str
    tags: List[str]
    page_num: int
    is_faved: bool
    is_bookmarked: bool
    faves_count: int
    next_info: List[ServiceUrl]


class MangaRequest(BaseModel):
    title: str
    author: str
    tags: List[str]
    page_num: int
    next_info: List[ServiceUrl]


class MangaResponse(BaseModel):
    manga_id: str
    title: str
    author: str
    tags: List[str]
    page_num: int
    next_info: List[ServiceUrl]


class BookmarkRequest(BaseModel):
    manga_id: str


class HistoryRequest(BaseModel):
    manga_id: str
    page_num: int


class TagRequest(BaseModel):
    tags: List[str]


class TagResponse(BaseModel):
    tags: List[str]

class FaveRequest(BaseModel):
    manga_id: str
