import datetime
from typing import List

from domain.history import History

from repository.db import DB


class HistoryDB(DB):
    def __init__(self):
        super().__init__('history')

    def add_history_user(self, manga_id: str, user_id: str, page_ratio: float) -> History:
        created_at = datetime.datetime.now()
        tm = History(manga_id=manga_id, user_id=user_id, page_ratio=page_ratio, created_at=created_at)
        self.insert(dict(tm))
        return tm
    
    def find_by_user_id(self, user_id: str) -> List[History]:
        res = self.find_query({'user_id': user_id})
        return [History(**r) for r in res if r is not None]

history_db = HistoryDB()
