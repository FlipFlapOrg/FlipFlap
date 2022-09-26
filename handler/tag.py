from typing import List
from handler.schema import TagResponse

from repository.tag_user import tag_user_db


# POST /{user_id}/tags
def add_user_tags(user_id: str, tags: List[str]) -> TagResponse:
    tag_user_db.delete_by_user_id(user_id)
    ts = tag_user_db.add_tags_user(user_id=user_id, tags=tags)
    return TagResponse(tags=[tag.tag for tag in ts])

# GET /{user_id}/tags
def get_user_tags(user_id: str) -> TagResponse:
    ts = tag_user_db.find_by_user_id(user_id)
    if ts is None:
        return TagResponse(tags=[])
    return TagResponse(tags=[tag.tag for tag in ts])
