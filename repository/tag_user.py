from typing import List

from domain.tag_user import TagUser

from repository.db import DB


class TagUserDB(DB):
    def __init__(self):
        super().__init__('tag_user')

    def add_tag_user(self, user_id: str, tag: str) -> TagUser:
        tm = TagUser(user_id=user_id, tag=tag)
        self.insert(dict(tm))
        return tm
    
    def add_tags_user(self, user_id: str, tags: List[str]) -> List[TagUser]:
        tms = [TagUser(user_id=user_id, tag=tag) for tag in tags]
        self.insert_many([dict(tm) for tm in tms])
        return tms
    
    def delete_by_user_id(self, user_id: str):
        self.delete({'user_id': user_id})
    
    def find_by_user_id(self, user_id: str) -> List[TagUser]:
        res = self.find_query({'user_id': user_id})
        return [TagUser(**r) for r in res if r is not None]

tag_user_db = TagUserDB()
