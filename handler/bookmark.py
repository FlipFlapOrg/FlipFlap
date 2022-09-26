from typing import List, Optional
from handler.schema import UserMangaResponse, BookmarkRequest

from fastapi import HTTPException, status

from repository.bookmark import bookmark_db
from repository.manga import manga_db


# GET /users/{user_id}/bookmarks
def get_user_bookmarks(user_id: str) -> List[UserMangaResponse]:
    return bookmark_db.get_bookmarks(user_id=user_id)


# POST /users/{user_id}/bookmarks
def add_user_bookmark(req: BookmarkRequest, user_id: str) -> UserMangaResponse:
    res = bookmark_db.add_bookmark(user_id=user_id, manga_id=req.manga_id)
    if res is None:
        raise HTTPException(status=status.HTTP_409_CONFLICT,
                            detail="Conflict with existing bookmark.")
    m = manga_db.find_by_id(manga_id=req.manga_id)
    if m is None:
        raise HTTPException(status=status.HTTP_404_NOT_FOUND,
                            detail="Manga not found.")
    return UserMangaResponse(
        manga_id=m.manga_id,
        title=m.title,
        author=m.author,
        tags=[],  # TODO: implement this
        manga_url=m.manga_url,
        is_faved=False,  # TODO: implement this
        is_bookmarked=True,
    )


# DELETE /users/{user_id}/bookmarks
def delete_user_bookmark(req: BookmarkRequest, user_id: str) -> None:
    bookmark_db.delete_bookmark(user_id=user_id, manga_id=req.manga_id)
    return None
