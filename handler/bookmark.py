from typing import List, Optional

from fastapi import HTTPException, status
from repository.bookmark import bookmark_db

from handler.manga import get_manga
from handler.schema import BookmarkRequest, UserMangaResponse


# GET /users/{user_id}/bookmarks
def get_user_bookmarks(user_id: str) -> List[UserMangaResponse]:
    return bookmark_db.get_bookmarks(user_id=user_id)


# POST /users/{user_id}/bookmarks
def add_user_bookmark(req: BookmarkRequest, user_id: str) -> UserMangaResponse:
    res = bookmark_db.add_bookmark(user_id=user_id, manga_id=req.manga_id)
    if res == False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Conflict with existing bookmark.")
    m = get_manga(manga_id=req.manga_id, user_id=user_id)
    return UserMangaResponse(
        manga_id=m.manga_id,
        title=m.title,
        author=m.author,
        tags=m.tags,
        page_num=m.page_num,
        manga_url=m.manga_url,
        is_faved=False,  # TODO: implement this
        is_bookmarked=True,
    )


# DELETE /users/{user_id}/bookmarks
def delete_user_bookmark(req: BookmarkRequest, user_id: str) -> None:
    bookmark_db.delete_bookmark(user_id=user_id, manga_id=req.manga_id)
    return None
