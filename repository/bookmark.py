import uuid
from typing import List, Optional

from domain.bookmark import Bookmark
from domain.manga import Manga
from handler.schema import UserMangaResponse

from repository.db import DB


class BookmarkDB(DB):
    def __init__(self):
        super().__init__('bookmark')

    def add_bookmark(self, user_id: str, manga_id: str) -> Optional[str]:
        res = self.insert_ignore(dict(user_id=user_id, manga_id=manga_id), [
                                 'user_id', 'manga_id'])
        if res == False:
            return None
        return res

    def delete_bookmark(self, user_id: str, manga_id: str) -> None:
        self.delete(dict(user_id=user_id, manga_id=manga_id))

    def is_bookmark(self, user_id: str, manga_id: str) -> bool:
        res = self.find_one(dict(user_id=user_id, manga_id=manga_id))
        return res is not None

    def get_bookmarks(self, user_id: str) -> List[UserMangaResponse]:
        res = self.query(
            'SELECT * FROM bookmark INNER JOIN manga ON bookmark.manga_id = manga.manga_id WHERE user_id = :user_id', {'user_id': user_id})
        # for r in res:
        #     print(dict(r))

        return [UserMangaResponse(
            manga_id=r['manga_id'],
            title=r['title'],
            author=r['author'],
            tags=[],
            manga_url=r['manga_url'],
            is_faved=False,  # TODO: implement this
            is_bookmarked=True,
        ) for r in res]


bookmark_db = BookmarkDB()
