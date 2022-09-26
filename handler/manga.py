import os
import shutil
from typing import List

from PIL import Image
from fastapi import HTTPException, UploadFile
from repository.manga import manga_db
from repository.tag_manga import tag_manga_db

from handler.schema import MangaRequest, MangaResponse, UserMangaResponse


# GET /manga/recommend
def get_recommendation(user_id: str) -> UserMangaResponse:
    return UserMangaResponse(
        manga_id="4ed8e4ab-50c2-4e87-abf1-ebf2cc87dcf1",
        title="One Piece",
        author="Eiichiro Oda",
        image_url=["https://i.pinimg.com/originals/4c/50/38/4c50386d57d207a960058fcc8a5609a8.jpg",
                   "https://qph.cf2.quoracdn.net/main-qimg-835ac26be15950837045ba53cca30845-lq"],
        tags=["action", "adventure", "comedy", "fantasy", "shounen"],
        is_faved=True,
        is_bookmarked=False
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
        title=req.title, author=req.author, page_num=req.page_num)
    for tag in req.tags:
        tag_manga_db.add_tag_manga(manga_id=manga.manga_id, tag=tag)
    return MangaResponse(
        manga_id=manga.manga_id,
        title=manga.title,
        author=manga.author,
        tags=req.tags,
        page_num=manga.page_num,
    )

# GET /manga/{manga_id}
def get_manga(manga_id: str) -> MangaResponse:
    manga = manga_db.find_by_id(manga_id)
    if manga is None:
        raise HTTPException(status_code=404, detail="Manga not found.")
    tags = tag_manga_db.find_by_manga_id(manga_id)
    if tags is None:
        tags = []
    return MangaResponse(
        manga_id=manga.manga_id,
        title=manga.title,
        author=manga.author,
        tags=[t.tag for t in tags],
        page_num=manga.page_num,
    )
