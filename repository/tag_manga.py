from typing import List

from domain.tag_manga import TagManga

from repository.db import DB


class TagMangaDB(DB):
    def __init__(self):
        super().__init__('tag_manga')

    def add_tag_manga(self, manga_id: str, tag: str) -> TagManga:
        tm = TagManga(manga_id=manga_id, tag=tag)
        self.insert(dict(tm))
        return tm
    
    def add_tags_manga(self, manga_id: str, tags: List[str]) -> List[TagManga]:
        tms = [TagManga(manga_id=manga_id, tag=tag) for tag in tags]
        self.insert_many([dict(tm) for tm in tms])
        return tms
    
    def find_by_manga_id(self, manga_id: str) -> List[TagManga]:
        res = self.find_query({'manga_id': manga_id})
        return [TagManga(**r) for r in res if r is not None]

tag_manga_db = TagMangaDB()
