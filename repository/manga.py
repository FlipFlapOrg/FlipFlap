import uuid
from typing import Optional

from domain.manga import Manga

from repository.db import DB


class MangaDB(DB):
    def __init__(self):
        super().__init__('manga')

    def add_manga(self, title: str, author: str, page_num: int) -> Manga:
        manga_id = uuid.uuid4().hex
        m = Manga(manga_id=manga_id, title=title,
                  author=author, page_num=page_num)
        self.insert(dict(m))
        return m

    def find_by_id(self, manga_id: str) -> Optional[Manga]:
        res = self.find_one({'manga_id': manga_id})
        return Manga(**res) if res else None

    def find_by_title(self, title: str) -> Optional[Manga]:
        res = self.find_one({'title': title})
        return Manga(**res) if res else None

manga_db = MangaDB()
