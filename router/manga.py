import os
from typing import List, Optional

from fastapi import APIRouter, File, Header, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from handler.manga import (add_manga, get_manga, get_recommendation,
                           manga_upload)
from handler.schema import MangaRequest, MangaResponse, UserMangaResponse

router = APIRouter()


@router.get("/recommend", response_model=UserMangaResponse, response_model_exclude_none=True)
async def get_recommend(user_id: Optional[str] = Header(default=None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="User ID is required.")
    return get_recommendation(user_id=user_id)


@router.post("/", response_model=MangaResponse, response_model_exclude_none=True)
async def post_manga(req: MangaRequest):
    return add_manga(req)


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def post_upload(manga_id: str, files: List[UploadFile] = File(...)):
    print(manga_id)
    manga_upload(manga_id, files)
    return {"message": "success"}


@router.get("/{manga_id}", response_model=UserMangaResponse, response_model_exclude_none=True)
async def get_manga_id(manga_id: str, user_id: Optional[str] = Header(default=None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="User ID is required.")
    return get_manga(manga_id=manga_id, user_id=user_id)


@router.get("/{manga_id}/image/{page_num}")
async def get_manga_image(manga_id: str, page_num: int) -> FileResponse:
    filename = f"/srv/data/{manga_id}/{page_num}.jpeg"
    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(filename)
