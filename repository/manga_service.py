from typing import List

from domain.manga_service import MangaService

from repository.db import DB


class MangaServiceDB(DB):
    def __init__(self):
        super().__init__('manga_service')

    def add_manga_service(self, manga_id: str, service_name: str, url: str) -> MangaService:
        tm = MangaService(manga_id=manga_id, service_name=service_name, url=url)
        self.insert(dict(tm))
        return tm
    
    def find_by_manga_id(self, manga_id: str) -> List[MangaService]:
        res = self.find_query({'manga_id': manga_id})
        return [MangaService(**r) for r in res if r is not None]

manga_service_db = MangaServiceDB()
