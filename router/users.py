from typing import List, Optional

from domain.history import History
from fastapi import APIRouter, HTTPException, status
from handler.bookmark import (add_user_bookmark, delete_user_bookmark,
                              get_user_bookmarks)
from handler.faves import add_user_fave, remove_user_fave
from handler.history import add_history
from handler.schema import (BookmarkRequest, FaveRequest, HistoryRequest,
                            TagRequest, TagResponse, UserMangaResponse)
from handler.tag import add_user_tags, get_user_tags

router = APIRouter()


@router.get("/{user_id}/bookmarks", response_model=List[UserMangaResponse])
async def get_bookmarks(user_id: str):
    return get_user_bookmarks(user_id=user_id)


@router.post("/{user_id}/bookmarks", response_model=UserMangaResponse)
async def post_bookmark(req: BookmarkRequest, user_id: str):
    return add_user_bookmark(req=req, user_id=user_id)


@router.delete("/{user_id}/bookmarks", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bookmark(req: BookmarkRequest, user_id: str):
    delete_user_bookmark(req=req, user_id=user_id)
    return None


@router.post("/{user_id}/faves", status_code=status.HTTP_201_CREATED)
async def post_faves(req: FaveRequest, user_id: str):
    add_user_fave(req=req, user_id=user_id)
    return {"message": "Successfully added bookmark."}


@router.delete("/{user_id}/faves", status_code=status.HTTP_204_NO_CONTENT)
async def delete_faves(req: FaveRequest, user_id: str):
    remove_user_fave(req=req, user_id=user_id)
    return None


@router.post("/{user_id}/history", status_code=status.HTTP_201_CREATED, response_model=History)
async def post_history(user_id: str, req: HistoryRequest):
    return add_history(user_id=user_id, manga_id=req.manga_id)


@router.post("/{user_id}/tags", status_code=status.HTTP_201_CREATED, response_model=TagResponse)
async def post_tags(user_id: str, req: TagRequest):
    return add_user_tags(user_id=user_id, tags=req.tags)


@router.get("/{user_id}/tags", response_model=TagResponse)
async def get_tags(user_id: str):
    return get_user_tags(user_id=user_id)
