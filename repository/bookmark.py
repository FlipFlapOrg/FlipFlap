from collections import defaultdict
import datetime
from typing import List

from domain.bookmark import Bookmark
from handler.schema import ServiceUrl, UserMangaResponse

from repository.db import DB


class BookmarkDB(DB):
    def __init__(self):
        super().__init__('bookmark')

    def add_bookmark(self, user_id: str, manga_id: str) -> bool:
        created_at = datetime.datetime.now()
        bookmark = Bookmark(manga_id=manga_id,
                            user_id=user_id, created_at=created_at)
        res = self.insert_ignore(dict(bookmark), ['user_id', 'manga_id'])
        if res == False:
            return False
        return True

    def delete_bookmark(self, user_id: str, manga_id: str) -> None:
        self.delete(dict(user_id=user_id, manga_id=manga_id))

    def is_bookmark(self, user_id: str, manga_id: str) -> bool:
        res = self.find_one(dict(user_id=user_id, manga_id=manga_id))
        return res is not None

    # TODO: serviceに移動したい
    def get_bookmarks(self, user_id: str) -> List[UserMangaResponse]:
        res = self.query(
            'SELECT * FROM bookmark INNER JOIN manga ON bookmark.manga_id = manga.manga_id WHERE user_id = :user_id', {'user_id': user_id})

        tag_res = self.query(
            'SELECT * FROM tag_manga WHERE manga_id IN (SELECT manga_id FROM bookmark WHERE user_id = :user_id)', {'user_id': user_id})
        tags = defaultdict(list)
        for tag in tag_res:
            if tag is None:
                continue
            tags[tag['manga_id']].append(tag['tag'])

        service_res = self.query(
            'SELECT * FROM manga_service WHERE manga_id IN (SELECT manga_id FROM bookmark WHERE user_id = :user_id)', {'user_id': user_id})
        services = defaultdict(list)
        for service in service_res:
            if service is None:
                continue
            services[service['manga_id']].append(
                ServiceUrl(service_name=service['service_name'], url=service['url']))

        # TODO: left outer joinで書き直す
        fav_res = self.query(
            'SELECT * FROM faves WHERE user_id = :user_id AND manga_id IN (SELECT manga_id FROM bookmark WHERE user_id = :user_id)', {'user_id': user_id})
        faves = defaultdict(lambda: False)
        for fav in fav_res:
            if fav is None:
                continue
            faves[fav['manga_id']] = True

        count_faves_res = self.query(
            'SELECT manga_id, COUNT(*) c FROM faves WHERE manga_id IN (SELECT manga_id FROM bookmark WHERE user_id = :user_id) GROUP BY manga_id', {'user_id': user_id})
        count_faves = defaultdict(lambda: 0)
        for count_fave in count_faves_res:
            if count_fave is None:
                continue
            count_faves[count_fave['manga_id']] = count_fave['c']

        return [UserMangaResponse(
            manga_id=r['manga_id'],
            title=r['title'],
            author=r['author'],
            tags=tags[r['manga_id']],
            page_num=r['page_num'],
            is_faved=faves[r['manga_id']],
            is_bookmarked=True,
            faves_count=count_faves[r['manga_id']],
            next_info=services[r['manga_id']]
        ) for r in res if r is not None]


bookmark_db = BookmarkDB()
