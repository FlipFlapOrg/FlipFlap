from typing import List, Optional
from handler.schema import UserMangaResponse, BookmarkRequest

from repository.bookmark import bookmark_db
from repository.manga import manga_db


def get_user_bookmarks(user_id: str) -> List[UserMangaResponse]:
    res = bookmark_db.get_bookmarks(user_id=user_id)
    return res


def add_user_bookmark(req: BookmarkRequest) -> Optional[UserMangaResponse]:
    res = bookmark_db.add_bookmark(user_id=req.user_id, manga_id=req.manga_id)
    if res is None:
        return None
    m = manga_db.find_by_id(manga_id=req.manga_id)
    if m is None:
        return None
    return UserMangaResponse(
        manga_id=m.manga_id,
        title=m.title,
        author=m.author,
        tags=m.tags,
        manga_url=m.manga_url,
        is_faved=False,  # TODO: implement this
        is_bookmarked=True,
    )


def delete_user_bookmark(req: BookmarkRequest) -> None:
    bookmark_db.delete_bookmark(req.user_id, req.manga_id)
    return None
