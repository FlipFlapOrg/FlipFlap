from typing import List
from handler.schema import UserMangaResponse, BookmarkRequest


def get_user_bookmarks(user_id: str) -> List[UserMangaResponse]:
    return []


def add_user_bookmark(req: BookmarkRequest) -> List[UserMangaResponse]:
    return []


def delete_user_bookmark(req: BookmarkRequest) -> None:
    return None
