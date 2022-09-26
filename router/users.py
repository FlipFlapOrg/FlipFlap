from typing import List, Optional

from fastapi import APIRouter, status, HTTPException
from handler.bookmark import (
    get_user_bookmarks, add_user_bookmark, delete_user_bookmark)
from handler.schema import UserMangaResponse, BookmarkRequest

router = APIRouter()


@router.get("/{user_id}/bookmarks", response_model=List[UserMangaResponse])
async def get_bookmarks(user_id: str):
    return get_user_bookmarks(user_id=user_id)


@router.post("/{user_id}/bookmarks", response_model=UserMangaResponse)
async def post_bookmark(req: BookmarkRequest):
    res = add_user_bookmark(req)
    if res is None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Conflict with existing bookmark.")
    return add_user_bookmark(req)


@router.delete("/{user_id}/bookmarks", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bookmark(req: BookmarkRequest):
    return delete_user_bookmark(req)
