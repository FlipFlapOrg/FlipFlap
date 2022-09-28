from fastapi import HTTPException
from repository.history import history_db
from repository.manga import manga_db


# POST /user/{user_id}/history
def add_history(user_id: str, manga_id: str, page_num: int):
    manga = manga_db.find_by_id(manga_id)
    if manga is None:
        raise HTTPException(status_code=400, detail="Manga not found.")
    page_ratio = page_num / manga.page_num * 100
    return history_db.add_history_user(manga_id=manga_id, user_id=user_id, page_ratio=page_ratio)
