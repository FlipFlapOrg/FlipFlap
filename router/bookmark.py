from typing import List, Optional

from fastapi import APIRouter, Header, HTTPException
from handler.bookmark import (get_user_bookmarks)
from handler.schema import UserMangaResponse

router = APIRouter()


@router.get("/users/{user_id}/bookmarks", response_model=List[UserMangaResponse])
async def get_bookmarks(user_id: Optional[str] = Header(default=None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="User ID is required.")
    return get_user_bookmarks(user_id=user_id)
