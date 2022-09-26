from typing import List, Optional

from fastapi import APIRouter, Header, HTTPException
from handler.manga import get_recommendation
from handler.schema import MangaResponse

router = APIRouter()


@router.get("/recommend", response_model=MangaResponse)
async def get_recommend(user_id: Optional[str] = Header(default=None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="User ID is required.")
    return get_recommendation(user_id=user_id)
