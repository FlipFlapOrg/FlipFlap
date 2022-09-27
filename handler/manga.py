import os
import random
from typing import List

from fastapi import HTTPException, UploadFile
from PIL import Image
from domain.manga_service import MangaService
from repository.bookmark import bookmark_db
from repository.faves import faves_db
from repository.manga import manga_db
from repository.manga_service import manga_service_db
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
    mss = manga_service_db.find_by_manga_id(manga_id)
    next_info = [{
        "service_name": ms.service_name,
        "url": ms.url,
    } for ms in mss]

    is_bookmarked = bookmark_db.is_bookmark(user_id=user_id, manga_id=manga_id)
    is_faved = faves_db.is_faves(user_id=user_id, manga_id=manga_id)
    fc = faves_db.count_faves(manga_id=manga_id)
    return UserMangaResponse(
        manga_id=manga.manga_id,
        title=manga.title,
        author=manga.author,
        tags=[t.tag for t in tags],
        page_num=manga.page_num,
        is_faved=is_faved,
        is_bookmarked=is_bookmarked,
        faves_count=fc,
        next_info=next_info,
    )


# POST /manga/upload
def manga_upload(manga_id: str, files: List[UploadFile]):
    manga = manga_db.find_by_id(manga_id)
    if manga is None:
        raise HTTPException(status_code=404, detail="Manga not found.")
    os.makedirs(f"/srv/data/{manga_id}", exist_ok=True)
    for i, f in enumerate(files):
        try:
            img = Image.open(f.file).convert('RGB')
            filename = f"/srv/data/{manga_id}/{i}.webp"
            print(filename)
            img.save(filename, "WEBP")
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, detail="internal server error")
        finally:
            f.file.close()
    # /srv/data/{manga_id} ディレクトリのファイルの数が page_num と一致するか確認する
    num = len(os.listdir(f"/srv/data/{manga_id}"))
    if num == manga.page_num:
        manga.is_completed = True
        manga_db.update(dict(manga), ["manga_id"])


# POST /manga
def add_manga(req: MangaRequest) -> MangaResponse:
    manga = manga_db.add_manga(
        title=req.title, author=req.author, page_num=req.page_num)

    tag_manga_db.add_tags_manga(manga_id=manga.manga_id, tags=req.tags)
    manga_service_db.add_manga_services(services=[MangaService(
        manga_id=manga.manga_id,
        service_name=nx.service_name,
        url=nx.url,
    ) for nx in req.next_info])

    return MangaResponse(
        manga_id=manga.manga_id,
        title=manga.title,
        author=manga.author,
        tags=req.tags,
        page_num=manga.page_num,
        next_info=req.next_info,
    )


# GET /manga/{manga_id}
def get_manga(manga_id: str, user_id: str) -> UserMangaResponse:
    manga = manga_db.find_by_id(manga_id)
    if manga is None:
        raise HTTPException(status_code=404, detail="Manga not found.")

    tags = tag_manga_db.find_by_manga_id(manga_id)
    if tags is None:
        tags = []
    mss = manga_service_db.find_by_manga_id(manga_id)
    next_info = [{
        "service_name": ms.service_name,
        "url": ms.url,
    } for ms in mss]

    is_bookmarked = bookmark_db.is_bookmark(user_id=user_id, manga_id=manga_id)
    is_faved = faves_db.is_faves(user_id=user_id, manga_id=manga_id)
    fc = faves_db.count_faves(manga_id=manga_id)

    return UserMangaResponse(
        manga_id=manga.manga_id,
        title=manga.title,
        author=manga.author,
        tags=[t.tag for t in tags],
        page_num=manga.page_num,
        is_faved=is_faved,
        is_bookmarked=is_bookmarked,
        faves_count=fc,
        next_info=next_info,
    )
