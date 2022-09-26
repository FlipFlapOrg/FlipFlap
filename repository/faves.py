import datetime

from domain.faves import Faves

from repository.db import DB


class FavesDB(DB):
    def __init__(self):
        super().__init__('faves')

    def add_faves(self, user_id: str, manga_id: str) -> bool:
        created_at = datetime.datetime.now()
        faves = Faves(manga_id=manga_id,
                            user_id=user_id, created_at=created_at)
        res = self.insert_ignore(dict(faves), ['user_id', 'manga_id'])
        if res == False:
            return False
        return True

    def delete_faves(self, user_id: str, manga_id: str) -> None:
        self.delete(dict(user_id=user_id, manga_id=manga_id))

    def is_faves(self, user_id: str, manga_id: str) -> bool:
        res = self.find_one(dict(user_id=user_id, manga_id=manga_id))
        return res is not None
    
    def count_faves(self, manga_id: str) -> int:
        res = self.query('SELECT COUNT(*) c FROM faves WHERE manga_id = :manga_id', {'manga_id': manga_id})
        if (r := next(res)) and 'c' in r and r['c'] is not None:
            return r['c']
        return -1


faves_db = FavesDB()
