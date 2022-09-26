import os
import random
from typing import List

from fastapi import HTTPException, UploadFile
from PIL import Image
from repository.bookmark import bookmark_db
from repository.faves import faves_db
from repository.manga import manga_db
from repository.tag_manga import tag_manga_db

from handler.schema import MangaRequest, MangaResponse, UserMangaResponse


# GET /manga/recommend
def get_recommendation(user_id: str) -> UserMangaResponse:
    all_manga = manga_db.find_all_manga()
    manga_id = random.choice(all_manga).manga_id
    
    manga = manga_db.find_by_id(manga_id)
    if manga is None:
        raise HTTPException(status_code=404, detail="Manga not found.")
    tags = tag_manga_db.find_by_manga_id(manga_id)
    if tags is None:
        tags = []

    is_bookmarked = bookmark_db.is_bookmark(user_id=user_id, manga_id=manga_id)
    is_faved = faves_db.is_faves(user_id=user_id, manga_id=manga_id)
    fc = faves_db.count_faves(manga_id=manga_id)
    return UserMangaResponse(
        manga_id=manga.manga_id,
        title=manga.title,
        author=manga.author,
        tags=[t.tag for t in tags],
        manga_url=manga.manga_url,
        page_num=manga.page_num,
        is_faved=is_faved,
        is_bookmarked=is_bookmarked,
        faves_count=fc,
    )


# POST /manga/upload
def manga_upload(manga_id: str, files: List[UploadFile]):
    manga = manga_db.find_by_id(manga_id)
    if manga is None:
        raise HTTPException(status_code=404, detail="Manga not found.")
    os.makedirs(f"/tmp/{manga_id}", exist_ok=True)
    for i, f in enumerate(files):
        try:
            img = Image.open(f.file).convert('RGB')
            filename = f"/tmp/{manga_id}/{i}.jpeg"
            print(filename)
            img.save(filename, "JPEG")
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, detail="internal server error")
        finally:
            f.file.close()
    # /tmp/{manga_id} ディレクトリのファイルの数が page_num と一致するか確認する
    num = len(os.listdir(f"/tmp/{manga_id}"))
    if num == manga.page_num:
        manga.is_completed = True
        manga_db.update(dict(manga), ["manga_id"])


# POST /manga
def add_manga(req: MangaRequest) -> MangaResponse:
    manga = manga_db.add_manga(
        title=req.title, author=req.author, page_num=req.page_num, manga_url=req.manga_url)
    for tag in req.tags:
        tag_manga_db.add_tag_manga(manga_id=manga.manga_id, tag=tag)
    return MangaResponse(
        manga_id=manga.manga_id,
        title=manga.title,
        author=manga.author,
        tags=req.tags,
        page_num=manga.page_num,
        manga_url=manga.manga_url,
    )


# GET /manga/{manga_id}
def get_manga(manga_id: str, user_id: str) -> UserMangaResponse:
    manga = manga_db.find_by_id(manga_id)
    if manga is None:
        raise HTTPException(status_code=404, detail="Manga not found.")
    tags = tag_manga_db.find_by_manga_id(manga_id)
    if tags is None:
        tags = []

    is_bookmarked = bookmark_db.is_bookmark(user_id=user_id, manga_id=manga_id)
    is_faved = faves_db.is_faves(user_id=user_id, manga_id=manga_id)
    fc = faves_db.count_faves(manga_id=manga_id)
    return UserMangaResponse(
        manga_id=manga.manga_id,
        title=manga.title,
        author=manga.author,
        tags=[t.tag for t in tags],
        manga_url=manga.manga_url,
        page_num=manga.page_num,
        is_faved=is_faved,
        is_bookmarked=is_bookmarked,
        faves_count=fc,
    )
